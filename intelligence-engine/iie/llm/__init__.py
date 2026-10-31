"""Model providers.

The engine never depends on a paid API. Supported providers:

* ``ollama``         local models through an Ollama server (default when reachable)
* ``openai_compat``  any local OpenAI-compatible server (llama.cpp server, LM Studio, vLLM)
* ``operator``       a person or external agent answers each structured request by file/UI;
                     answers are labelled with who gave them
* ``none``           no model; generation steps are skipped and marked as not performed

Every request is a structured task with a JSON schema. Outputs are validated
before use. A model never calls tools directly; the orchestrator decides tool use.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from typing import Any

import httpx

from ..schema import SchemaError, validate
from ..util import dumps, now_iso, sha256


class ModelUnavailable(RuntimeError):
    pass


class OperatorPending(RuntimeError):
    def __init__(self, task_ids: list[str]):
        super().__init__(f"Waiting for operator answers: {', '.join(task_ids)}")
        self.task_ids = task_ids


@dataclass
class GenTask:
    role: str
    purpose: str
    system: str
    prompt: str
    schema: dict
    project_id: str | None = None
    job_id: str | None = None
    temperature: float = 0.5
    max_tokens: int = 2000
    meta: dict = field(default_factory=dict)

    def request_key(self) -> str:
        return sha256(dumps([self.project_id, self.role, self.purpose, self.prompt, self.schema]))


def extract_json(text: str) -> Any:
    """Parse JSON from model output, tolerating surrounding prose or code fences."""
    text = (text or "").strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
    try:
        return json.loads(text)
    except ValueError:
        pass
    for open_ch, close_ch in (("{", "}"), ("[", "]")):
        start = text.find(open_ch)
        while start >= 0:
            depth, in_str, esc = 0, False, False
            for i in range(start, len(text)):
                ch = text[i]
                if in_str:
                    if esc:
                        esc = False
                    elif ch == "\\":
                        esc = True
                    elif ch == '"':
                        in_str = False
                    continue
                if ch == '"':
                    in_str = True
                elif ch == open_ch:
                    depth += 1
                elif ch == close_ch:
                    depth -= 1
                    if depth == 0:
                        try:
                            return json.loads(text[start : i + 1])
                        except ValueError:
                            break
            start = text.find(open_ch, start + 1)
    raise ValueError("No JSON object found in model output")


class Provider:
    name = "base"
    kind = "none"
    model: str | None = None

    def available(self) -> tuple[bool, str]:
        return False, "not configured"

    def generate(self, task: GenTask) -> dict:
        raise ModelUnavailable("No model provider configured.")

    def generate_many(self, tasks: list[GenTask]) -> list[dict]:
        return [self.generate(t) for t in tasks]

    def describe(self) -> dict:
        ok, why = self.available()
        return {"provider": self.name, "kind": self.kind, "model": self.model, "available": ok, "detail": why}


class NullProvider(Provider):
    name = "none"
    kind = "none"

    def available(self) -> tuple[bool, str]:
        return False, "no model configured; generation steps will be marked as not performed"


def _validated(task: GenTask, data: Any) -> dict:
    if isinstance(data, list) and task.schema.get("type") == "object":
        raise SchemaError("expected an object, got a list")
    validate(data, task.schema)
    return data


class OllamaProvider(Provider):
    name = "ollama"
    kind = "local"

    def __init__(self, url: str = "http://127.0.0.1:11434", model: str | None = None, timeout: float = 900):
        self.url = url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.last_stats: dict = {}

    def _client(self) -> httpx.Client:
        # trust_env=False keeps local traffic away from any outbound proxy.
        return httpx.Client(timeout=self.timeout, trust_env=False)

    def list_models(self) -> list[dict]:
        with self._client() as c:
            r = c.get(f"{self.url}/api/tags", timeout=5)
            r.raise_for_status()
            return r.json().get("models", [])

    def available(self) -> tuple[bool, str]:
        try:
            models = self.list_models()
        except Exception as e:  # noqa: BLE001
            return False, f"Ollama not reachable at {self.url}: {type(e).__name__}"
        names = [m.get("name") for m in models]
        if not names:
            return False, "Ollama is running but no models are installed (try: ollama pull qwen2.5:3b)"
        if self.model and self.model not in names:
            return False, f"model {self.model} not installed; installed: {', '.join(names)}"
        if not self.model:
            self.model = names[0]
        return True, f"{len(names)} model(s) installed; using {self.model}"

    def chat(self, system: str, prompt: str, schema: dict | None, temperature: float, max_tokens: int) -> str:
        body: dict[str, Any] = {
            "model": self.model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            "stream": False,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }
        if schema is not None:
            body["format"] = schema
        t0 = time.time()
        with self._client() as c:
            r = c.post(f"{self.url}/api/chat", json=body)
            r.raise_for_status()
            data = r.json()
        ev, dur = data.get("eval_count") or 0, (data.get("eval_duration") or 0) / 1e9
        self.last_stats = {"latency_s": time.time() - t0, "eval_count": ev,
                           "tokens_per_sec": (ev / dur) if dur else None}
        return data.get("message", {}).get("content", "")

    def generate(self, task: GenTask) -> dict:
        ok, why = self.available()
        if not ok:
            raise ModelUnavailable(why)
        text = self.chat(task.system, task.prompt, task.schema, task.temperature, task.max_tokens)
        try:
            return _validated(task, extract_json(text))
        except (ValueError, SchemaError) as e:
            repair = (task.prompt + f"\n\nYour previous answer was invalid ({e}). Return only JSON that matches the schema.")
            text = self.chat(task.system, repair, task.schema, 0.2, task.max_tokens)
            return _validated(task, extract_json(text))

    def embed(self, texts: list[str], model: str) -> list[list[float]]:
        with self._client() as c:
            r = c.post(f"{self.url}/api/embed", json={"model": model, "input": texts})
            r.raise_for_status()
            return r.json().get("embeddings", [])


class OpenAICompatProvider(Provider):
    name = "openai_compat"
    kind = "local"

    def __init__(self, url: str, model: str | None, api_key: str | None = None, timeout: float = 900):
        self.url = url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.timeout = timeout

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

    def available(self) -> tuple[bool, str]:
        try:
            with httpx.Client(timeout=5, trust_env=False) as c:
                r = c.get(f"{self.url}/v1/models", headers=self._headers())
                r.raise_for_status()
                ids = [m.get("id") for m in r.json().get("data", [])]
        except Exception as e:  # noqa: BLE001
            return False, f"server not reachable at {self.url}: {type(e).__name__}"
        if not self.model and ids:
            self.model = ids[0]
        return (bool(self.model), f"models: {', '.join(i for i in ids if i)}")

    def generate(self, task: GenTask) -> dict:
        ok, why = self.available()
        if not ok:
            raise ModelUnavailable(why)
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": task.system + "\nReturn only JSON."},
                {"role": "user", "content": task.prompt + "\n\nJSON schema:\n" + json.dumps(task.schema)},
            ],
            "temperature": task.temperature,
            "max_tokens": task.max_tokens,
            "response_format": {"type": "json_object"},
        }
        with httpx.Client(timeout=self.timeout, trust_env=False) as c:
            r = c.post(f"{self.url}/v1/chat/completions", json=body, headers=self._headers())
            r.raise_for_status()
            text = r.json()["choices"][0]["message"]["content"]
        return _validated(task, extract_json(text))


class OperatorProvider(Provider):
    """Structured requests answered by a person or an external agent.

    Each request is stored in ``operator_tasks``. The job pauses until an answer is
    submitted with ``iie operator answer`` or the web UI. Answers are validated
    against the schema and stored with the name of whoever answered.
    """

    name = "operator"
    kind = "operator"

    def __init__(self, db, label: str = "operator"):
        self.db = db
        self.model = label

    def available(self) -> tuple[bool, str]:
        return True, "answers come from a named operator through the operator queue"

    def generate(self, task: GenTask) -> dict:
        return self.generate_many([task])[0]

    def generate_many(self, tasks: list[GenTask]) -> list[dict]:
        results: list[dict | None] = []
        pending: list[str] = []
        for t in tasks:
            key = t.request_key()
            row = self.db.one("operator_tasks", "request_key=? ORDER BY created_at DESC", (key,))
            if row and row["status"] == "answered":
                results.append(_validated(t, row["answer"]))
                continue
            if row is None:
                with self.db.tx():
                    tid = self.db.insert("operator_tasks", {
                        "project_id": t.project_id, "job_id": t.job_id, "role": t.role, "purpose": t.purpose,
                        "request_key": key, "prompt": {"system": t.system, "prompt": t.prompt}, "schema": t.schema,
                        "status": "pending",
                    })
            else:
                tid = row["id"]
            pending.append(tid)
            results.append(None)
        if pending:
            raise OperatorPending(pending)
        return results  # type: ignore[return-value]


def answer_operator_task(db, task_id: str, answer: Any, answered_by: str) -> None:
    row = db.get("operator_tasks", task_id)
    if row is None:
        raise KeyError(task_id)
    if not answered_by or answered_by.strip().lower() in ("", "model", "system"):
        raise ValueError("answered_by must name the person or agent answering.")
    validate(answer, row["schema"])
    db.update("operator_tasks", task_id, {"status": "answered", "answer": answer,
                                          "answered_by": answered_by, "answered_at": now_iso()})


def get_provider(settings, db) -> Provider:
    choice = settings.model_provider
    if choice in ("ollama", "auto"):
        p = OllamaProvider(settings.ollama_url, settings.ollama_model or _benchmarked_default(db))
        if choice == "ollama" or p.available()[0]:
            return p
    if choice in ("openai_compat", "auto") and settings.openai_compat_url:
        p2 = OpenAICompatProvider(settings.openai_compat_url, settings.openai_compat_model,
                                  settings.secret("openai_compat_key"))
        if choice == "openai_compat" or p2.available()[0]:
            return p2
    if choice == "operator":
        return OperatorProvider(db)
    return NullProvider()


def _benchmarked_default(db) -> str | None:
    if db is None:
        return None
    row = db.one("benchmarks", "provider='ollama' AND json_valid=1 AND correct=1 ORDER BY tokens_per_sec DESC", ())
    return row["model"] if row else None
