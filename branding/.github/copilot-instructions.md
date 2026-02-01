# AI Copilot Instructions - Detroit Automation Academy Branding

## Project Overview

Detroit Automation Academy is launching a comprehensive brand identity system for a Detroit-based automation/robotics education nonprofit. The project spans 3 phases (Jan 31 - Feb 10, 2026) with a public launch February 10, 2026.

**Brand Promise:** "Automation skills for Detroit's future, built by Detroiters"  
**Visual Strategy:** Modern + Industrial + Community-Driven

---

## Critical Context for AI Agents

### Architecture: The 3-Phase Strategy
1. **Phase 1 (Jan 31-Feb 3):** Strategy documentation + 5 logo concepts + color palettes (CURRENT)
2. **Phase 2 (Feb 4-6):** Logo refinement, icon system, website redesign, brand guidelines
3. **Phase 3 (Feb 7-10):** Website launch, social templates, print collateral, team training

Each phase depends on the previous phase's decisions. Never suggest changes that violate prior phase agreements without explicit approval.

### The Brand Pillars Framework
All design decisions must align with these 4 interdependent pillars:
- **Accessibility:** Inclusive, welcoming, clear communication (no jargon)
- **Innovation:** Cutting-edge, future-focused, experimental aesthetic
- **Community:** Detroit-centric, locally-built, celebrating collaboration
- **Practicality:** Professional credibility for grants/sponsorships, industry-aligned

When evaluating or creating content, ask: "Which pillar does this support?"

### Color Palette Decision Structure
Three competing options exist—each option spans multiple files for consistency:
- **Option A (RECOMMENDED):** Tech Forward (Blue #0066CC + Rust #CC5522 + Lime #66CC00)
- **Option B:** Detroit Pride (Red #CC2233 + Purple #663399 + Yellow #FFCC00)
- **Option C:** Modern Tech (Cyan #0099CC + Charcoal #333333 + Neon Green #99FF33)

All colors verified for WCAG AA accessibility. Reference specific hex codes from `COLOR_PALETTE_DEVELOPMENT.md` when working with colors.

### Logo Concepts: 5 Directions, One Decision
Each concept embodies different brand messaging:
1. **Gear + Circuit** → Tech precision + automation
2. **Phoenix/Rise** → Growth + Detroit momentum
3. **Detroit Circuit Network** → Local connectivity + tech
4. **Learning Spiral** → Continuous education + curriculum
5. **Hands + Technology** → Practical, human-centered skills

Reference the full concept details (visual elements, mood, variations) in `LOGO_CONCEPT_FRAMEWORK.md`—don't oversimplify to avoid losing strategic rationale.

---

## Developer Workflows

### Document-First Development
This project is documentation-heavy. Changes flow through markdown files first:
1. **Read the full context** from the relevant .md file before suggesting changes
2. **Update strategy documents first**, then cascade changes to supporting documents
3. **Use the Implementation Checklist** as source of truth for task status (✅/🔄/❌)

### Key File Dependencies
- [README.md](../README.md) → Master index and quick-start guide (update first for navigation)
- [BRAND_STRATEGY.md](../BRAND_STRATEGY.md) → Foundation for all decisions (never contradict without updates here)
- [LOGO_CONCEPT_FRAMEWORK.md](../LOGO_CONCEPT_FRAMEWORK.md) → Framework for design evaluation
- [COLOR_PALETTE_DEVELOPMENT.md](../COLOR_PALETTE_DEVELOPMENT.md) → Technical specs for all colors
- [IMPLEMENTATION_CHECKLIST.md](../IMPLEMENTATION_CHECKLIST.md) → Task tracking and approval status
- [concepts/](../concepts/) → Design mockups (will expand in Phase 2)

### Cross-Document Consistency
When editing, verify consistency across:
- Hex color codes (must match exactly across all documents)
- Deadline dates (Phase 1: Feb 3, Phase 2: Feb 6, Phase 3: Feb 10)
- Concept names and descriptions (maintain exact phrasing)
- Owner assignments (@CTO, @Admin, @COO, @SCHEDULER)

---

## Project-Specific Conventions

### Naming & Structure
- **Logo concepts** use format: `NN-ConceptName/` (e.g., `01-Gear-Circuit/`)
- **Color codes** always specified as: Color Name, HEX, RGB, Pantone, CMYK
- **Document headers** include: Version, Date, Status, Owner, Deadline
- **Checklists** use: [x] completed, [ ] pending, 🔄 in-progress, ❌ blocked

### Status Labels & Emoji
Use consistent indicators:
- ✅ COMPLETE / ✅ READY
- 🔄 IN PROGRESS / 🔄 PENDING APPROVAL
- ❌ BLOCKED
- ⭐ RECOMMENDED
- 🔴 ACTIVE / ⚠️ AT RISK

### Decision Documentation
Every strategic choice must reference its rationale. Include:
- **Why this direction** (connects to brand pillars)
- **What it communicates** (messaging impact)
- **Constraints addressed** (monochrome, scale, professionalism)
- **Design notes** (specific technical implementation guidance)

---

## Integration Points & Dependencies

### Stakeholder Groups
Update communications when making decisions affecting:
- **Students (14-25):** Need modern, approachable, inspiring visuals
- **Parents/Guardians:** Need professional, trustworthy, results-focused identity
- **Employers/Partners:** Need technical credibility and industry alignment
- **Sponsors/Donors:** Need professional, mission-aligned, organized presentation
- **Media/Public:** Need visually compelling, newsworthy Detroit story

### Cross-Team Coordination
- @CTO = Design lead (strategy, aesthetics, concepts)
- @Admin = Project coordinator (timeline, checklists, communication)
- @COO = Resources (budget, vendor management)
- @SCHEDULER = Timeline management (deadlines, phase gates)

Coordinate changes that affect timelines or resource allocation.

---

## What NOT to Do

- ❌ **Don't suggest "more modern" without specific examples** → Reference existing design language or concepts
- ❌ **Don't ignore the 4 brand pillars** → Every suggestion must align with Accessibility, Innovation, Community, Practicality
- ❌ **Don't create new concepts without framework** → Use `LOGO_CONCEPT_FRAMEWORK.md` structure
- ❌ **Don't invent color specs** → Use only colors from `COLOR_PALETTE_DEVELOPMENT.md` with exact hex codes
- ❌ **Don't bypass the checklist** → Mark progress in `IMPLEMENTATION_CHECKLIST.md` as source of truth
- ❌ **Don't suggest design changes that contradict Phase 1 decisions** → Request Phase 1 updates first

---

## Examples of Correct Patterns

✅ **Correct:** "The phoenix concept aligns with the 'Innovation' and 'Community' pillars by suggesting upward Detroit momentum. Reference [LOGO_CONCEPT_FRAMEWORK.md](../LOGO_CONCEPT_FRAMEWORK.md) Concept 2 for specific visual elements."

✅ **Correct:** "For color implementation, use Electric Blue (#0066CC) as primary per Option A in [COLOR_PALETTE_DEVELOPMENT.md](../COLOR_PALETTE_DEVELOPMENT.md), verified WCAG AA compliant."

✅ **Correct:** "Update the Implementation Checklist: move 'Logo design direction' from ✅ COMPLETE to ✅ COMPLETE & READY FOR DESIGN PHASE as of [DATE]."

---

## Quick Reference

| Document | Purpose | Update Frequency |
|----------|---------|------------------|
| README.md | Navigation & quick-start | Weekly |
| BRAND_STRATEGY.md | Foundation (don't change) | Never in Phase 1 |
| LOGO_CONCEPT_FRAMEWORK.md | Design reference | As concepts evolve |
| COLOR_PALETTE_DEVELOPMENT.md | Technical specs | Only for refinement |
| IMPLEMENTATION_CHECKLIST.md | Task tracking | Daily |
| concepts/ | Design deliverables | Phase 2 expansion |

---

**Last Updated:** January 31, 2026  
**Next Review:** February 3, 2026 (end of Phase 1)
