"""Approval enforcement for outside actions."""
import httpx
import pytest

from iie import approvals
from iie.approvals import ApprovalRequired
from iie.guard import IndependenceViolation
from iie.orchestrator import Engine


def test_gated_tool_needs_user_approval_once_per_use(settings, tmp_path):
    e = Engine(settings, offline=True)
    sent = []
    e.tools.transport = httpx.MockTransport(lambda r: sent.append(r) or httpx.Response(200))
    args = {"url": "https://hooks.example.com/x", "payload": {"text": "hello"}}
    with pytest.raises(ApprovalRequired) as ei:
        e.tools.call("webhook_post", args, actor="experiment_designer")
    aid = ei.value.approval_id
    assert not sent
    with pytest.raises(PermissionError):
        approvals.decide(e.db, aid, True, actor="decision_director")  # agents cannot approve
    approvals.decide(e.db, aid, True, actor="user")
    assert e.tools.call("webhook_post", args, actor="experiment_designer") == 200
    assert len(sent) == 1
    with pytest.raises(ApprovalRequired):  # approval is single use
        e.tools.call("webhook_post", args, actor="experiment_designer")


def test_denied_action_stays_blocked(settings):
    e = Engine(settings, offline=True)
    args = {"item": "CNC router", "amount": 180000, "currency": "INR", "supplier": "X"}
    with pytest.raises(ApprovalRequired) as ei:
        e.tools.call("record_purchase_order", args, actor="materials_manufacturing")
    approvals.decide(e.db, ei.value.approval_id, False, actor="user")
    with pytest.raises(PermissionError) as ei2:
        e.tools.call("record_purchase_order", args, actor="materials_manufacturing")
    assert "denied" in str(ei2.value)


def test_approved_payload_must_match_exactly(settings):
    e = Engine(settings, offline=True)
    a = {"to": "a@example.com", "subject": "hi", "body": "x"}
    with pytest.raises(ApprovalRequired) as ei:
        e.tools.call("send_email", a, actor="buyer_researcher")
    approvals.decide(e.db, ei.value.approval_id, True, "user")
    changed = dict(a, to="someone-else@example.com")
    with pytest.raises(ApprovalRequired):
        e.tools.call("send_email", changed, actor="buyer_researcher")


def test_private_file_read_requires_approval_and_never_reaches_excluded(settings, tmp_path):
    e = Engine(settings, offline=True)
    f = tmp_path / "quote.txt"
    f.write_text("supplier quote ₹450")
    with pytest.raises(ApprovalRequired) as ei:
        e.tools.call("read_private_file", {"path": str(f)}, actor="commercial_analyst")
    approvals.decide(e.db, ei.value.approval_id, True, "user")
    assert "₹450" in e.tools.call("read_private_file", {"path": str(f)}, actor="commercial_analyst")
    bad = tmp_path / "Studio_Brain" / "x.txt"
    bad.parent.mkdir()
    bad.write_text("no")
    with pytest.raises(ApprovalRequired) as ei:
        e.tools.call("read_private_file", {"path": str(bad)}, actor="commercial_analyst")
    approvals.decide(e.db, ei.value.approval_id, True, "user")
    with pytest.raises(IndependenceViolation):
        e.tools.call("read_private_file", {"path": str(bad)}, actor="commercial_analyst")
