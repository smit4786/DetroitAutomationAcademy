# AI Copilot Instructions - Detroit Automation Academy

## Project Overview

**Detroit Automation Academy** is a comprehensive educational robotics curriculum with three progressive phases (Python → CAD → Autonomous Systems) plus extensive event coordination, administrative infrastructure, and branding systems. This is a **multi-domain monorepo** spanning education, operations, and brand strategy.

**Context**: Founded in Detroit, nonprofit focused on underrepresented students in automation/robotics. Major event activation: Boys & Girls Club (BGC) Feb 4, 2026.

---

## "Big Picture" Architecture

### The Core Curriculum (Education Domain)
```
phase1/ → GPIO control (RPi.GPIO, LED/button patterns)
phase2/ → CAD design (parametric Python, G-code/STL export)
phase3/ → Autonomous systems (rover simulation, navigation)
docs/   → 6+ comprehensive guides (quick_start, phase guides, API reference)
```
- **Key Integration**: Each phase builds on previous concepts; progression is irreversible
- **Hardware Abstraction Gap**: Phase 1 currently tied to Raspberry Pi; mock GPIO needed for cross-platform dev
- **Why This Structure**: Educational modularization + isolated learning objectives allow students to start mid-curriculum

### Multi-Domain Repository (Non-Curriculum)
1. **Event Infrastructure** (`BGC_EVENT_*.md`, `event_status_monitor.py`)
   - Real-time GitHub enrollment tracking + milestone notifications
   - Dashboard generation for event day projectors
   - Coordinates with calendar/calendar imports

2. **Administrative Workflows** (`ADMINISTRATIVE_COORDINATION_PLAN.md`, expense sync, calendar events)
   - Financial tracking (`daa_expense_sync.py` syncs Google Sheets ↔ accounting)
   - Event scheduling & Google Calendar integration
   - Staff coordination checklists

3. **Branding System** (`branding/` folder)
   - 3-phase brand identity rollout (Jan 31 - Feb 10, 2026)
   - Logo concepts, color palettes, typography systems
   - Production-quality design standards
   - **Critical Deadline**: Phase 1 (Feb 3) feeds Phase 2 (Feb 4-6)

4. **Hardware Assets** (`.stl`, `.gcode` files)
   - 3D print files (rover chassis, sensor mount, tokens) for Bambu Lab
   - Laser cutting patterns for Epilog Laser Fusion Maker

### Data Flow & Integration Points
```
GitHub Issues (enrollment) → event_status_monitor.py → BGC_EVENT_STATUS_DASHBOARD.html
                          → Real-time metrics for event staff

Google Sheets (expenses) → daa_expense_sync.py → QuickBooks/Wave (accounting)
                        → Financial reporting for grants/sponsors

Google Calendar (events) → import_calendar_to_google.py → Team sync
                        → Student enrollment confirmations
```

---

## Critical Project Conventions

### Status & Timeline Awareness
- **Current Date**: Feb 4, 2026 (TODAY = B&G Club event day + Phase 2 brand design kickoff)
- **Phase 1 (Complete)**: Curriculum dev, 3 demo events, brand strategy
- **Phase 2 (Active)**: Logo refinement, icon system, website redesign, brand guidelines
- **Phase 3 (Pending)**: Website launch, social templates, print collateral (Feb 7-10)
- **90-Day Roadmap**: Error handling, hardware abstraction, Docker containerization (from CTO assessment)

**Key Implication**: Changes that affect branding must coordinate with phase deadlines. Changes to event workflows must preserve GitHub Actions integration points.

### Direction Mapping Convention (Phase 3)
All rover navigation uses cardinal direction integers:
```python
0 = North (+y movement)
1 = East (+x movement)
2 = South (-y movement)
3 = West (-x movement)
```
**Rule**: Direction values ALWAYS use modulo 4 (e.g., `direction = (direction + 1) % 4`). Never deviate from this. Example: [phase3/autonomous_rover.py](phase3/autonomous_rover.py#L14-L55)

### Debugging Challenges = Intentional Bugs (Pedagogical)
Files like `challenge_1_rover_debug.py` contain **deliberate bugs marked with `TODO` comments**. These are NOT defects to fix—they're core teaching tools. Each bug teaches a specific lesson:
- **Coordinate inversions**: North moves `+y`, not `-y`
- **Swapped return values**: `(y, x)` instead of `(x, y)`
- **Inverted control logic**: `turn_left()` using `+1` instead of `-1`
- **Resource leaks**: Battery increasing instead of decreasing

**Preserve exactly as-is**. When adding challenges, follow this pattern: clear docstring, TODO above each bug, matching correct implementation in phase file for reference.

### Documentation-Driven Development
This project is unusually documentation-heavy. Markdown files are **source of truth** for architecture decisions:
- **Strategy files** override code decisions if conflicts exist
- Update `MASTER_DOCUMENT_INDEX.md` whenever you create/modify key docs
- `docs/INDEX.md` is role-based navigation hub (maintain for all user types: students, instructors, event planners, developers)
- Cross-reference: Always link `.md` files when referencing design rationale

### Naming Conventions
- **Markdown headers**: Use emoji for visual scanning (`# 📋 Section Name`)
- **Status indicators**: `✅ COMPLETE`, `🔄 IN PROGRESS`, `❌ BLOCKED`, `⭐ RECOMMENDED`
- **Checklists**: `[x]` = done, `[ ]` = pending, `🔄` = in-progress
- **Color codes**: Always specify as `Color Name, #HEX, RGB` (e.g., `Blue, #0066CC, rgb(0,102,204)`)
- **File naming**: Descriptive + purpose clear (not `doc1.md` but `BGC_EVENT_STATUS_DASHBOARD_README.md`)

---

## Developer Workflows

### Building & Testing
```bash
# Format code
black .

# Lint
flake8 .

# Run all tests (32 tests, 100% pass rate)
pytest test_examples.py

# Run specific phase tests
pytest test_examples.py -k "phase1" -v
```

### Adding New Code
1. **New curriculum feature**: Add to `phaseN/` with docstrings + tests
2. **Debugging challenge**: Create `challenge_X_<topic>.py` with `TODO` comments marking bugs
3. **Admin workflow**: Use `event_status_monitor.py` as pattern (dataclass + API client + CLI args)
4. **Hardware asset**: Generate Python parametric model → export G-code/STL → add to `activations/`

### Git Workflow & Pre-Commit Hooks
8 pre-commit hooks enforce consistency:
- **Black formatting** (88 char line length)
- **Flake8 linting** (max-line-length=88, ignore E203,W503)
- **Bandit security scan** (skip tests/)
- **YAML/JSON/TOML validation**
- **Trailing whitespace removal**
- **isort import sorting**

**Critical**: Pre-commit hooks run automatically on `git commit`. All commits must pass. No bypassing with `--no-verify` without justification.

### Python Version Support
Code must support **Python 3.8–3.11**. Test against all versions in CI/CD pipeline. Use `from __future__ import annotations` for type hints if needed.

---

## Integration Architecture

### GitHub Actions (Future)
Event enrollment tracking integrates with GitHub Issues:
- Uses GitHub API to query issues labeled `"enrollment"`
- Parses issue metadata for student info, program, background
- Real-time dashboard generation (no database, GitHub Issues as source of truth)
- **Why**: Leverages GitHub's free tier; no backend server needed

### Google Services Integration
Multiple scripts sync project state to Google ecosystem:
- **Google Sheets** (`daa_expense_sync.py`): Two-way expense sync for grant accounting
- **Google Calendar** (`import_calendar_to_google.py`): Event scheduling + enrollment confirmations
- **Service accounts**: Stored securely; use `GOOGLE_CLOUD_WALKTHROUGH.md` for setup

**Pattern**: Always use service accounts with minimal IAM permissions. Never commit credentials.

### External Hardware
- **Raspberry Pi 4+**: Phase 1 GPIO examples (cross-platform mock needed for dev)
- **Bambu Lab X1 Carbon / A1**: Phase 2 3D print targets (100×100×100mm designs typical)
- **Epilog Laser Fusion Maker**: Phase 2 laser cutting (30-40W CO2, 610×305mm bed)
  - G-code comments include: power (25-30%), speed (40%), material type
  - Test vectors on scrap material first (critical safety!)

---

## Architecture Decision Log (Why This Structure)

### Why Monorepo?
Curriculum tightly couples with event logistics (enrollment tracking, scheduling), brand identity (marketing materials for B&G event), and admin workflows (expense tracking, team coordination). Monorepo avoids sync friction across these domains.

### Why Phase-Based Modules Over Single Codebase?
1. **Educational isolation**: Students can focus on one concept without "big system" cognitive load
2. **Progressive complexity**: Each phase adds one new domain (GPIO → geometry → navigation)
3. **Cross-phase independence**: Instructors can teach Phase 2 without Phase 1 knowledge
4. **Testing flexibility**: Phase tests run independently; failures isolate to one domain

### Why GitHub Issues for Enrollment Instead of Database?
- **Leverage free GitHub tier**: No backend infrastructure cost
- **Transparent to team**: All enrollment data visible in Issues; no secret database
- **Audit trail**: GitHub issue history = automatic enrollment log
- **Integrates with brand/event timeline**: Can create issues from calendar events, link to promotional tweets

### Why Google Sheets for Expenses Instead of Dedicated Tool?
- **Grant accountants already use**: QuickBooks/Wave is standard in nonprofit accounting; Google Sheets bridges that gap
- **Two-way sync**: Real-time expense visibility + flexibility for grant accountants to adjust categories
- **Cost**: Free tier supports this project's scale (< 1000 transactions/month)

---

## Key Files & Their Roles

| File/Folder | Role | Owner | Update Frequency |
|---|---|---|---|
| `README.md` | Master entry point + role-based navigation | Docs Lead | Monthly |
| `docs/INDEX.md` | Student/instructor/dev navigation hub | Docs Lead | As features added |
| `docs/phase1_guide.md` | Phase 1 learning objectives + hardware specs | Instructor | Semester start |
| `phase1/led_blink.py` | GPIO output pattern example | Curriculum Dev | Rarely |
| `challenge_1_rover_debug.py` | Pedagogical debugging exercise (preserve bugs!) | Curriculum Dev | New challenges quarterly |
| `test_examples.py` | 32 automated tests (100% pass rate) | QA | With each feature |
| `pyproject.toml` | Dependencies + Python version support | Dev Lead | When adding packages |
| `.pre-commit-config.yaml` | Code quality guardrails | Dev Lead | Tool version updates |
| `event_status_monitor.py` | Real-time enrollment tracking (GitHub API client) | Admin Dev | Before events |
| `daa_expense_sync.py` | Google Sheets ↔ accounting sync | Finance Dev | Monthly |
| `CTO_TECHNICAL_ROADMAP.md` | 90-day technical strategy + capacity planning | CTO | Monthly |
| `branding/README.md` | Brand system entry point + 3-phase rollout plan | Brand Lead | Phase deadlines |
| `branding/LOGO_CONCEPT_FRAMEWORK.md` | 5 logo concepts + evaluation criteria | Design Lead | Pre-phase reviews |
| `MASTER_DOCUMENT_INDEX.md` | Complete doc inventory + file purposes | Project Mgr | Quarterly |

---

## Common Tasks & Patterns

### Task: Add New Phase 1 GPIO Example
```python
# In phase1/new_example.py
"""Phase 1 GPIO Example: [Clear topic]

Hardware:
- Raspberry Pi 4+
- GPIO pins [specify which]
- [Hardware list]

Learning objective: [What students will understand]
"""

import RPi.GPIO as GPIO
# ... your code ...
# Run: python3 phase1/new_example.py (or pytest test_examples.py::test_new_feature)
```
Then: Add test case to `test_examples.py`, update `docs/phase1_guide.md`, add to `docs/api_reference.md`.

### Task: Add New Debugging Challenge
1. Create `challenge_X_<topic>.py` with intentional bugs marked `# TODO: [bug domain]`
2. Each bug teaches ONE lesson (don't stack bugs in same line)
3. Provide matching correct implementation in `phase3/autonomous_rover.py` (or appropriate phase)
4. Document bug in docstring: "Students should notice [symptom] because of [root cause]"
5. Add to testing guide in `docs/`

### Task: Update Event Dashboard for New Metrics
1. Modify `event_status_monitor.py` to query new GitHub Issue field
2. Update `test_event_dashboard.py` with new metric test case
3. Update `BGC_EVENT_STATUS_DASHBOARD_README.md` with new dashboard section
4. Test locally: `python3 event_status_monitor.py --token [token] --continuous`

### Task: Sync New Expense Category to Accounting
1. Add to Google Sheets template (category + formula)
2. Update expense category enum in `daa_expense_sync.py`
3. Run sync: `python3 daa_expense_sync.py`
4. Verify in QuickBooks/Wave UI

---

## Avoid These Mistakes

1. **Don't remove `TODO` comments** from challenge files—they mark pedagogical bugs, not defects
2. **Don't break direction mapping**: North = 0, East = 1, South = 2, West = 3 (modulo 4 always)
3. **Don't commit credentials**: Google service account keys go in `.env`, never in `.git`
4. **Don't skip pre-commit hooks**: They catch formatting/security issues automatically
5. **Don't update only code**: Documentation must stay synchronized or future developers miss context
6. **Don't ignore phase deadlines**: Branding Phase 2 (Feb 4-6) depends on Phase 1 (Feb 3) decisions
7. **Don't hardcode GPIO pins**: Use config files or environment variables for cross-platform dev
8. **Don't merge event dashboard changes without coordinator approval**: Impacts live event display

---

## When in Doubt

- **Architecture question?** → Read [CTO_TECHNICAL_ROADMAP.md](../CTO_TECHNICAL_ROADMAP.md) (decisions + rationale)
- **Curriculum question?** → Check [docs/api_reference.md](../docs/api_reference.md) + phase guides
- **Event/admin workflow?** → See [MASTER_DOCUMENT_INDEX.md](../MASTER_DOCUMENT_INDEX.md) + specific workflow file
- **Brand/design question?** → Review [branding/README.md](../branding/README.md) + phase timeline
- **Code pattern?** → Reference corresponding phase file (led_blink.py, cad_design.py, autonomous_rover.py)
