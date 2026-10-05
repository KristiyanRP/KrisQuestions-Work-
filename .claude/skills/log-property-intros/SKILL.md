---
name: log-property-intros
description: Log new property deals from the Hay Wain "Property Introductions" Outlook group (zzintroduction@hay-wain.com) into Carta CRM. Reads each group email and its PDF brochure, checks Carta for an existing deal on the same property, and creates the missing ones as Real Estate deals with the overview, address, sector, tenure, price, NIY, area and other metrics filled in, leaving Next Steps and Reasons for Discount for the team. Use whenever someone asks to log, sync, update or catch up Carta with new property intros / introductions / opportunities from email, check the intros group for new deals, backfill deals that were missed, or run the scheduled Property Introductions sync, even if they don't name the group or Carta explicitly.
---

# Log Property Introductions into Carta

The team forwards every new property opportunity to the **Property Introductions**
Microsoft 365 group. This skill turns those emails into Carta CRM deals so the
pipeline is complete without anyone retyping brochures.

The run is **idempotent**: it re-reads a window of recent group emails every time
and only creates deals Carta doesn't already have. Overlapping windows are the
point: a missed or failed run is healed by the next one, and running twice
does no harm.

## Modes

- **Interactive** (someone asked in chat): show the plan, then create. If more
  than 10 new deals are found, list them and ask before creating.
- **Scheduled** (the prompt says "scheduled run"): nobody is watching, so do not
  ask questions. Create up to 10 new deals, and list any extra ones in the report.
  They will be picked up next run.
- **Dry run** (the prompt says "dry run", "preview", or "what would you log"):
  do everything except `create_deal`, and report what *would* be created.

Defaults: look back **14 days**. If the user gives a date ("since 1 August",
"backfill the last 3 months"), use that instead.

## Hard rules (and why)

- **Only ever call `crm:create_deal`.** Never update, delete or link existing
  records, and never change fields or stages. Humans own existing deals. The repo's
  permission hook auto-approves `create_deal` only; any other write stops for a
  person's approval.
- **Never fill `hwg_next_steps` (Next Steps) or `HWRE_reasons_for_discount`
  (Reasons for Discount).** Those record the team's judgement, not facts from the
  email.
- **Only facts from the source.** Leave a field blank rather than guess. A wrong
  price or yield pollutes pipeline reports more than an empty cell does. Derived
  numbers are fine when the arithmetic is unambiguous (e.g. £ psf = price ÷ area).
- **When unsure whether a deal already exists, don't create it.** Put it under
  "Needs review" instead. A duplicate is more work to clean up than a 10-second
  manual check.

## Step 1: Connect

1. Carta requires `welcome` → `get_current_user` → `read_resource
   carta://business-glossary` before other calls (the server enforces this order).
   Note which Carta user is connected: new deals are created under that user.
2. Call `crm:get_deal_fields` once (via `crm_read_tool`) and confirm the field IDs
   in the mapping below still exist. If one has been renamed or removed, skip that
   field and mention it in the report rather than failing the run.

## Step 2: Collect the group's emails

The group mailbox **cannot be opened directly**: `mailboxOwnerEmail:
zzintroduction@hay-wain.com` fails with `ErrorGroupIsUsedInNonGroupURI`. Don't try.
Instead, search the connected user's own mailbox, which holds a copy of every group
post *provided they follow the group in their inbox* (Outlook → Groups → Property
Introductions → Follow in inbox). Without that, only posts that also name them in
To/CC arrive.

```
outlook_email_search(recipient="zzintroduction@hay-wain.com",
                     afterDateTime="<window start>", limit=25)
```

Page with `offset` while `nextOffset` is returned. `recipient` matches To *and* CC,
which matters because colleagues often send to a person and CC the group. Read each
message with `read_resource(uri=<mail:/// uri>)`.

**Read the attachments.** Brochures and IMs (`application/pdf`, not `isInline`)
usually hold the numbers; the email body is often just a signature. Read them with
`read_resource(uri=<attachment uri>, startPage=1, endPage=8)`. That is normally
enough for the investment summary and tenancy schedule. Skip inline images (logos,
signatures). If the details are behind a data-room link you can't open, work from
the body and say so in the report.

## Step 3: Work out which deals each email contains

Group emails are messy. Judge each one on its content, not its subject line:

- **Forwarded chains:** the HWG colleague's note sits at the top ("To log and
  discount – income too dry"). The original agent or sponsor email sits below in
  the `From:/Sent:/Subject:` block. The agent is the introducer, not the colleague.
- **Subjects mislead.** "FW: Camden / Basingstoke" turned out to be a follow-up on
  an existing Camden deal plus a *new* Bracknell office/car-park deal whose IM was
  attached. One email can hold zero, one or several deals.
- **Not deals:** event invites, portfolio-company admin (board actions, exclusivity
  paperwork on a deal already in progress), group-membership notices, and replies
  that add no new property. List them under "Not a deal" with a few words on why.
- **Same property sent twice** (re-sends, or a reminder weeks later) is one deal.
  Collapse duplicates inside the batch before checking Carta.

For each deal, pin down the property's identity: building or scheme name, street
address, town, **postcode**, and main tenant if single-let.

## Step 4: Check Carta for an existing deal

Names in Carta rarely match the email exactly. Example: the email says "CMR Surgical
Ltd, Lancaster Way Business Park, CB6 3NX" and Carta has "CMR Surgical, Lancaster Way
Business Park, Ely". So run several cheap searches (`crm:search_deals` via
`crm_read_tool`, `limit` 10) and judge the hits yourself:

1. Postcode: `filters: [{field_id: "company.company_location", operator: "contains", value: "<full postcode, else outward code>"}]`
2. Most distinctive name token: building name, street or tenant (e.g. "Chapel Walks",
   "CMR"), with `operator: "contains"` on `company.company_name`.
3. Free text: `query: "<town> <distinctive word>"` as a last resort.

Filters in one call are ANDed, so run each one as a separate call.

- **Same address or building** = already in Carta, even if the stage is Lapsed or
  the name is formatted differently. Report it with its Carta link and don't touch it.
  If the email carries materially new information (new price, revised terms), say so
  in one line so a human can update the record.
- **Same street or estate but a different unit or number** = a different deal.
- **Can't tell** = Needs review.

## Step 5: Build the deal

Match the conventions of the team's existing Real Estate deals:

| Carta field | Payload key | What to put |
|---|---|---|
| Deal name | `company.name` | `<Building or tenant>, <street/estate>, <town or postcode district>`. Examples: "Oval House, SW9", "10 Chapel Walks, Manchester", "CMR Surgical, Lancaster Way Business Park, Ely". Under ~60 chars. Use the scheme name alone if there's no address yet (e.g. "Redhill"). |
| Industry | `company.industry` | "Commercial Real Estate"; "Residential Real Estate" for resi/BTR/PBSA; "Hotel / Leisure Real Estate" for hotels. |
| Location | `company.location` | Full address with postcode, as given. |
| Description | `company.description` | 60-120 words, metrics-dense, plain text: what and where, size, tenure, tenancy (tenants, rent, £ psf, WAULT to expiry/breaks), quoting price, NIY, £ psf, capex, business plan/upside, and anything notable (e.g. "two prior sale processes collapsed"). |
| **Deal Overview** | `comment` | 1-3 plain-English sentences wrapped in `<p>…</p>`: what it is, where, and the headline price/yield. The quick read on the deal card. |
| Added date | `addedAt` | The email's `receivedDateTime` date (ISO), i.e. when the intro reached the team. |
| Pipeline / stage | `pipelineId`, `stageId` | `hay_wain_primary`, `hwg_identified` (Identified). Always. |
| Investment Strategy | `fields.HW_investment_strategy` | "Real Estate" |
| Deal Type | `fields.HWRE_deal_type` | "Equity" (acquisition / JV equity, the usual case), "Debt" (loan or lending request), "Hybrid Capital" (pref equity, mezz). |
| Introduction Type | `fields.HW_introduction_type` | "On Market": agent-run sale (brochure, "instructed to seek offers", "launched"). "Off-Market": shared privately or exclusively before or instead of marketing. "Direct": straight from an owner, vendor, sponsor or developer with no agent process. Omit if unclear. |
| Sector | `fields.HWRE_Sector` | One of: Office, Hotel, Residential, Retail, Industrial, Other, Portfolio, Mixed-Use, PBSA/HMO. Industrial covers logistics, R&D and trade. Several assets = Portfolio. Car parks, self-storage, data centres = Other unless clearly one of the above. |
| Tenure | `fields.HWRE_Tenure` | Freehold, Leasehold or Long-Leasehold (described as long leasehold / virtual freehold, or roughly 99+ years unexpired). |
| Purchase/Asking Price | `fields.HWRE_purchaseasking_price` | Whole pounds (13550000). Quoting, guide, "offers in excess of" or agreed price. For a range, use the lower end and mention the range in the description. |
| Capital Valuation (psf) | `fields.HWRE_capital_valuation` | £ psf as stated, else price ÷ total area, rounded to whole pounds. |
| Total Area | `fields.HWRE_total_area` | sq ft. NIA if given, else GIA. Convert sq m × 10.764. Rounded. |
| NIY | `fields.HWRE_NIY` | Percent as a number (5.5 for 5.50%). Only if stated; don't compute. |
| CAPEX | `fields.HWRE_capex` | Whole pounds, if stated (all-in figure if both are given). |
| Equity Requirement | `fields.HWRE_equity_requirement` | Whole pounds, if stated. |
| Expected Returns | `fields.HWRE_expected_returns` | IRR % as a number, if stated. Prefer levered and say which in the description. |
| Expected Hold Period | `fields.HWRE_expected_hold_period` | Text, e.g. "5 years", if stated. |
| Advisers Company | `fields.hwg_advisers_company` | `["<agent firm's web domain>"]` from the introducing agent's email address (e.g. `["logixproperty.com"]`). Skip personal domains (gmail etc.) and hay-wain.com. |

Do not send `hwg_next_steps`, `HWRE_reasons_for_discount`, `dealLead` (it defaults
to the connected user), `tags`, or any `HW_PE_*` / private-equity field.

Shape of the call (`crm_call_tool`, with a one-line `summary` naming the property):

```json
{
  "name": "crm:create_deal",
  "arguments": {
    "pipelineId": "hay_wain_primary",
    "stageId": "hwg_identified",
    "addedAt": "2026-10-02",
    "comment": "<p>…</p>",
    "company": {"name": "…", "industry": "Commercial Real Estate", "location": "…", "description": "…"},
    "fields": {"HW_investment_strategy": "Real Estate", "HWRE_deal_type": "Equity", "…": "…"}
  }
}
```

Omit keys you have no value for. Don't send nulls or empty strings, because an empty
string *clears* a Carta field. If a create fails, report the error and carry on with
the next deal.

## Step 6: Report

End every run with this report. In scheduled mode it is the only thing a person
reads, so make it skimmable:

```
## Property Introductions → Carta (<window start> to <today>)
Scanned N emails · Created X · Already in Carta Y · Needs review Z · Not a deal W

### Created
- [<Deal name>](<carta url>): <sector>, <price>, <NIY>. From <agent/firm> via <HWG sender>, <date>.
  HWG note: "<colleague's comment, verbatim>"   ← only if there was one

### Already in Carta
- <Deal name>: [Carta](<url>), <stage>. <one line if the email has new info>

### Needs review
- <Email subject> (<date>): <why, e.g. "possible match: Oval House, SW9">

### Not a deal
- <Email subject>: <why>
```

Quote the colleague's note verbatim when it signals a decision ("To log and
discount – lot size"), so whoever fills Reasons for Discount and moves the stage has
it to hand. Don't act on it yourself.
