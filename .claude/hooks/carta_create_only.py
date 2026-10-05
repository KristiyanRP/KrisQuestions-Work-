#!/usr/bin/env python3
"""PreToolUse guard for mcp__Carta__crm_call_tool.

Auto-approves Carta CRM *create_deal* calls so the scheduled
log-property-intros run can add deals without a person clicking "allow".
Every other CRM write (update, delete, link, schema changes...) gets no
decision from this hook, so it falls through to the normal permission prompt.
"""
import json
import sys

AUTO_APPROVED = {"create_deal"}

try:
    payload = json.load(sys.stdin)
except (json.JSONDecodeError, ValueError):
    sys.exit(0)

name = str((payload.get("tool_input") or {}).get("name", ""))
if name.removeprefix("crm:") in AUTO_APPROVED:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": "log-property-intros: creating a new Carta deal",
        }
    }))
