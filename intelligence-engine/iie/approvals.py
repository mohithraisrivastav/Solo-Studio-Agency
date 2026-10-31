"""Approval enforcement for actions with outside effects.

Any tool whose side effect is in ``GATED_KINDS`` runs only when a user has
approved that exact payload (matched by hash), and each approval can be used once.
"""
from __future__ import annotations

from typing import Any

from .db import DB
from .util import dumps, now_iso, sha256

GATED_KINDS = {
    "purchase": "Make a purchase or place an order",
    "send_message": "Send an email, message, or webhook to anyone outside this machine",
    "publish": "Publish content anywhere public",
    "spend_money": "Commit or spend money",
    "modify_external_account": "Change anything in an external account",
    "access_private_data": "Read a private file outside the engine's storage",
    "irreversible": "Take an action that cannot be undone",
}

APPROVER_ACTORS = {"user"}


class ApprovalRequired(PermissionError):
    def __init__(self, approval_id: str, kind: str, reason: str):
        super().__init__(f"Approval {approval_id} needed for {kind}: {reason}")
        self.approval_id = approval_id
        self.kind = kind


def payload_hash(kind: str, payload: Any) -> str:
    return sha256(kind + "|" + dumps(payload))


def request(db: DB, kind: str, payload: Any, requested_by: str, reason: str, project_id: str | None = None) -> str:
    if kind not in GATED_KINDS:
        raise ValueError(f"Unknown gated action kind {kind}")
    h = payload_hash(kind, payload)
    existing = db.one("approvals", "payload_hash=? AND status='pending'", (h,))
    if existing:
        return existing["id"]
    with db.tx():
        aid = db.insert("approvals", {
            "project_id": project_id, "kind": kind, "payload": payload, "payload_hash": h, "status": "pending",
            "requested_by": requested_by, "reason": reason,
        })
        db.log(project_id, None, requested_by, "approval_requested", f"{kind}: {reason}", detail={"approval": aid})
    return aid


def decide(db: DB, approval_id: str, approve: bool, actor: str) -> None:
    if actor not in APPROVER_ACTORS:
        raise PermissionError(f"Only the user can approve or deny actions (got '{actor}').")
    row = db.get("approvals", approval_id)
    if row is None:
        raise KeyError(approval_id)
    if row["status"] != "pending":
        raise ValueError(f"Approval {approval_id} is already {row['status']}.")
    with db.tx():
        db.execute("UPDATE approvals SET status=?, decided_at=?, decided_by=? WHERE id=?",
                   ("approved" if approve else "denied", now_iso(), actor, approval_id))
        db.log(row["project_id"], None, actor, "approval_decided",
               f"{'approved' if approve else 'denied'} {row['kind']}", detail={"approval": approval_id})


def consume(db: DB, kind: str, payload: Any) -> dict | None:
    """Return and mark used an approved, unused approval for this exact payload."""
    h = payload_hash(kind, payload)
    with db.tx():
        row = db.one("approvals", "payload_hash=? AND status='approved' AND consumed=0", (h,))
        if row:
            db.execute("UPDATE approvals SET consumed=1 WHERE id=?", (row["id"],))
    return row


def require(db: DB, kind: str, payload: Any, requested_by: str, reason: str, project_id: str | None = None) -> dict:
    row = consume(db, kind, payload)
    if row:
        return row
    denied = db.one("approvals", "payload_hash=? AND status='denied'", (payload_hash(kind, payload),))
    if denied:
        raise PermissionError(f"The user denied this {kind} action (approval {denied['id']}).")
    aid = request(db, kind, payload, requested_by, reason, project_id)
    raise ApprovalRequired(aid, kind, reason)
