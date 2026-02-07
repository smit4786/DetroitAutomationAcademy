# ✅ BGC Event Dashboard — Go-Live README

**Go-Live Target:** 7:00 AM (Tomorrow)
**Domain:** detroitautomationacademy.com

---

## 🚀 Publish Priority: BGC Event Dashboard

This file is the **operational go-live checklist** for the BGC Event Dashboard and public launch.

### 1) Hosting & DNS (Complete by 5:30 AM)
- [ ] Confirm hosting provider and upload destination (web root).
- [ ] Place `BGC_EVENT_STATUS_DASHBOARD.html` at the public web root.
- [ ] Configure DNS for detroitautomationacademy.com:
	- [ ] A/AAAA records point to hosting IP(s)
	- [ ] `www` CNAME to apex domain
- [ ] Enable HTTPS (auto-cert or manual certificate).
- [ ] Verify HTTP → HTTPS redirect.

### 2) Dashboard Readiness (Complete by 6:00 AM)
- [ ] Validate enrollment data source (GitHub issues access).
- [ ] Confirm dashboard refresh interval and data pipeline.
- [ ] Run `test_event_dashboard.py` and verify success.
- [ ] Ensure `event_status_monitor.py` runs with `--continuous --notify`.

### 3) Launch Validation (Complete by 6:30 AM)
- [ ] Open https://detroitautomationacademy.com in a browser.
- [ ] Confirm dashboard loads quickly (under 2 seconds).
- [ ] Confirm styles match DAA branding.
- [ ] Confirm live enrollment data updates.

### 4) Go-Live (7:00 AM)
- [ ] Announce launch to internal team.
- [ ] Begin live monitoring from staff terminal.
- [ ] Keep a fallback static version ready if API limits occur.

---

## 📍 Emergency Fallbacks

If GitHub API limits or connectivity issues occur:
- Use the attendee-facing display only (static stats)
- Switch to local refresh mode with cached data
- Log incidents in `BGC_EVENT_STATUS_DASHBOARD_INDEX.md`

---

## 🧭 Quick Links

- Event Day Ops: `EVENT_DAY_DASHBOARD_README.md`
- Technical: `BGC_EVENT_DASHBOARD_INTEGRATION.md`
- Overview: `BGC_EVENT_STATUS_DASHBOARD.md`

---
---
# 🟦 Dashboard Tile Layout & Privacy (Feb 7, 2026)

## Tile-Based Dashboard Organization
- All dashboard elements are organized as responsive tiles:
  - Enrollment Tile: Shows total and today's enrollments (anonymized counts only)
  - Event Status Tile: Live event metrics (aggregate, no personal info)
  - Program Interest Tile: Breakdown by program (no participant names)
  - Agent Highlight Tile: Current active project agents (role/status only)
  - Admin Tile: Staff-only metrics (requires authentication)

## Privacy & Anonymization
- No full names, emails, or sensitive identifiers displayed
- All participant data is anonymized (counts, initials, or cohort numbers)
- Admin/staff tiles require secure authentication
- All tiles reviewed for privacy compliance before publishing
- Data sources (GitHub Issues, Google Sheets, Calendar) filtered to exclude personal info

## Example Tile Format
| Tile Name           | Data Shown                | Privacy Level   |
|---------------------|--------------------------|-----------------|
| Enrollment          | Total count, hourly rate | Public, anonymized |
| Event Status        | Aggregate metrics         | Public, anonymized |
| Program Interest    | Program breakdown         | Public, anonymized |
| Agent Highlight     | Role/status only          | Public, anonymized |
| Admin               | Staff metrics             | Restricted, authenticated |

## Implementation Notes
- Move dashboard files to dashboard/ folder for clarity
- Ensure all dashboard code and HTML use tile layout and anonymized data
- Reference [BGC_DASHBOARD_VISUAL_GUIDE.md](dashboard/BGC_DASHBOARD_VISUAL_GUIDE.md) for visual standards
- Reference [ADMINISTRATIVE_COORDINATION_PLAN.md](../ADMINISTRATIVE_COORDINATION_PLAN.md) for privacy workflow

---

**Owner:** CTO — Automated Technologies
**Status:** 🟡 In Progress (Go-Live in ~24 hours)
