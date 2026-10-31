"""Tool registry. Every call is logged; gated tools pass through the approval check first."""
from __future__ import annotations

import smtplib
import traceback
from dataclasses import dataclass
from email.message import EmailMessage
from typing import Any, Callable

import httpx

from . import approvals
from .db import DB
from .guard import SafeFS, check_url


@dataclass
class ToolSpec:
    name: str
    description: str
    side_effect: str | None  # one of approvals.GATED_KINDS or None
    fn: Callable[..., Any]


class ToolRunner:
    def __init__(self, db: DB, fs: SafeFS, settings, transport: httpx.BaseTransport | None = None):
        self.db = db
        self.fs = fs
        self.settings = settings
        self.transport = transport
        self.tools: dict[str, ToolSpec] = {}
        self._register_builtin()

    def register(self, spec: ToolSpec) -> None:
        self.tools[spec.name] = spec

    def call(self, name: str, args: dict, actor: str, project_id: str | None = None, job_id: str | None = None,
             reason: str = "") -> Any:
        spec = self.tools.get(name)
        if spec is None:
            raise KeyError(f"Unknown tool {name}")
        if spec.side_effect:
            approvals.require(self.db, spec.side_effect, {"tool": name, "args": args}, actor,
                              reason or spec.description, project_id)
        self.db.log(project_id, job_id, actor, "tool_call", f"{name}", tool=name,
                    detail={"args": {k: (v if len(str(v)) < 300 else str(v)[:300] + "…") for k, v in args.items()}})
        try:
            out = spec.fn(**args)
        except Exception as e:
            self.db.log(project_id, job_id, actor, "tool_error", f"{name}: {type(e).__name__}: {e}", tool=name,
                        detail={"trace": traceback.format_exc()[-1500:]})
            raise
        self.db.log(project_id, job_id, actor, "tool_result", f"{name} ok", tool=name)
        return out

    # built-in tools -------------------------------------------------------
    def _register_builtin(self) -> None:
        self.register(ToolSpec("write_workspace_file", "Write a local draft file inside the engine workspace",
                               None, self._write_workspace_file))
        self.register(ToolSpec("webhook_post", "POST a JSON message to an external URL", "send_message",
                               self._webhook_post))
        self.register(ToolSpec("send_email", "Send an email through the configured SMTP server", "send_message",
                               self._send_email))
        self.register(ToolSpec("record_purchase_order", "Record an approved purchase for the user to place",
                               "purchase", self._record_purchase))
        self.register(ToolSpec("read_private_file", "Read one user file outside the engine storage",
                               "access_private_data", self._read_private_file))

    def _write_workspace_file(self, relpath: str, text: str) -> str:
        p = self.fs.write_text(self.settings.workspace / relpath, text)
        return str(p)

    def _webhook_post(self, url: str, payload: dict) -> int:
        check_url(url)
        with httpx.Client(timeout=20, transport=self.transport) as c:
            r = c.post(url, json=payload)
            return r.status_code

    def _send_email(self, to: str, subject: str, body: str) -> str:
        host = self.settings.secret("smtp_host")
        if not host:
            raise RuntimeError("SMTP is not configured (set IIE_SMTP_HOST, IIE_SMTP_USER, IIE_SMTP_PASSWORD).")
        msg = EmailMessage()
        msg["To"], msg["Subject"] = to, subject
        msg["From"] = self.settings.secret("smtp_user") or "iie@localhost"
        msg.set_content(body)
        with smtplib.SMTP(host, 587, timeout=30) as s:
            s.starttls()
            if self.settings.secret("smtp_user"):
                s.login(self.settings.secret("smtp_user"), self.settings.secret("smtp_password") or "")
            s.send_message(msg)
        return "sent"

    def _record_purchase(self, item: str, amount: float, currency: str, supplier: str) -> str:
        # The engine never buys anything itself; it records the approved order for the user to place.
        p = self.fs.write_text(self.settings.workspace / "purchase_orders.txt",
                               f"APPROVED TO PLACE (by user): {item} | {amount} {currency} | {supplier}\n")
        return str(p)

    def _read_private_file(self, path: str) -> str:
        p = self.fs.grant_private_read(path)
        return self.fs.read_text(p)
