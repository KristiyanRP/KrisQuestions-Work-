# KrisQuestions-Work-
Repository for all questions regarding HW/Modella Work flows

## Property Introductions → Carta sync

Turns every deal posted to the **Property Introductions** Outlook group
(zzintroduction@hay-wain.com) into a Real Estate deal in Carta CRM. Deals that are
already in Carta are skipped. Next Steps and Reasons for Discount are always left
for the team to fill in.

| File | What it is |
|---|---|
| `.claude/skills/log-property-intros/SKILL.md` | The workflow: how to find group emails, read the brochures, check Carta for duplicates, which fields to fill, and the run report. |
| `.claude/settings.json` | Pre-approves the read-only Outlook and Carta tools so a scheduled run isn't blocked by permission prompts. |
| `.claude/hooks/carta_create_only.py` | Auto-approves Carta **create deal** calls only. Any other Carta write (update, delete, etc.) still asks a person. |

### One-time setup
1. In Outlook, open **Groups → Property Introductions** and choose **Follow in
   inbox**. The Microsoft 365 connector can't open the group mailbox itself; it
   sees group posts through your inbox copy.
2. Make sure the **Microsoft 365** and **Carta** connectors are connected in claude.ai.

### Running it
- On demand: in a Claude Code session on this repo, say "log new property intros"
  (or "dry run the property intros sync" to preview without creating anything).
- Catch-up: "log property intros since 1 June".
- Scheduled: a Routine that runs on weekday mornings with the prompt
  "Scheduled run: log new property intros from the last 14 days" and the Microsoft
  365 + Carta connectors attached. Each run re-checks two weeks of emails, so a
  missed run is picked up next time and nothing is ever logged twice.
