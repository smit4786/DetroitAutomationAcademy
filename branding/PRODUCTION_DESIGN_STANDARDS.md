# PRODUCTION DESIGN STANDARDS - Logo Concepts

**Document Version:** 1.0  
**Date:** January 31, 2026  
**Status:** Design Quality Framework  
**Owner:** @CTO  
**Purpose:** Establish minimum production values for all concept mockups

---

## Executive Summary

Current concept templates are strategic prototypes, NOT production-ready designs. This document defines the quality standards required for Feb 3 stakeholder presentation.

**Distinction:**
- ✅ **Strategic Template:** Demonstrates concept direction, validates metaphor clarity
- ❌ **NOT Production Quality:** Rough paths, inconsistent strokes, imprecise geometry, untested at scale

**February 3 Requirement:** HIGH-FIDELITY PRODUCTION MOCKUPS suitable for grant applications, corporate partnerships, and public launch marketing.

---

## AESTHETIC STANDARDS

### 1. Geometric Precision
**Standard:**
- All curves must be mathematically smooth (no wobbles, flat spots, or tangent breaks)
- Angles must be exact (30°, 45°, 60°, 90° where intended)
- Symmetry verified at pixel-perfect level in design tool
- No "eyeballed" proportions—use guidelines and snapping

**Testing:**
- Zoom to 400% → check for smooth curves
- Toggle fill/stroke visibility → check path quality
- Align to grid → verify intentional vs. accidental asymmetry

**Example Error:** Current template has hand-drawn gear teeth inconsistency (teeth angles vary, outer radius wavers)

### 2. Stroke Consistency
**Standard:**
- Primary strokes: 2-3px (at 1x scale), exact width specified
- Secondary details: 1.5px for refinement
- All strokes use "round" line cap and "round" line join (no sharp angles on endpoints)
- Stroke weight consistent across entire design (no variance unless intentional highlight)

**Testing:**
- Zoom in → verify all strokes same width
- Print to physical → check if readability maintained at small sizes
- View in monochrome → verify contrast sufficient without color

**Example Error:** Current template has inconsistent stroke widths (gear stroke 2.5px, circuit 2px, nodes unstropped)

### 3. Color Application
**Standard:**
- Primary color (#0066CC) for main mark/symbol (70% visual weight)
- Secondary color (#CC5522) for supporting detail (20% visual weight)
- Accent color (#66CC00) for energy/emphasis only (10% visual weight)
- All fills/strokes must use exact hex codes from `COLOR_PALETTE_DEVELOPMENT.md`
- Test contrast: all color pairs must meet WCAG AA (4.5:1 text, 3:1 graphics)

**Testing:**
- Export as monochrome → should remain clear
- Print at 0.5" → colors should still differentiate (avoid too-similar shades)
- View through colorblind simulator (Coblis) → all elements distinguishable

**Example Error:** Current template uses lime nodes at 0.7 opacity—production version needs solid, opaque colors

### 4. Scalability Verification
**Standard:**
- Design must be tested and optimized for 5 specific scales
- No detail so small it disappears at 0.5"
- No overly bold elements that dominate at 24"
- Line weights must scale proportionally with design
- Minimum line weight at smallest scale ≥ 0.75px (readable in print)

**Test Protocol:**
```
- 0.5": Business card size (minimum viable detail)
- 1": Standard web favicon/icon size
- 2": Website logo lockup size (primary use case)
- 6": Large signage/print size
- 24": Billboard/banner size (maximum detail still clear)
```

**Export Requirements:**
- Raster versions at 300 DPI for print at each scale
- Vector source (.AI or .SVG) must scale infinitely without degradation

**Example Error:** Current template would have circuit node dots disappear at 0.5" due to 3px fixed size

### 5. Visual Hierarchy Clarity
**Standard:**
- Single focal point immediately identifiable (usually center of composition)
- Primary element (gear, phoenix form, skyline) dominates visual attention (60-70% of composition)
- Secondary elements (circuit lines, accent details) support but don't compete (20-30%)
- Tertiary elements (nodes, background, context) recede (remaining 10%)
- When viewed in monochrome, hierarchy should still be clear

**Testing:**
- Show monochrome version at arm's length → main symbol immediately clear?
- Show at 0.5" → can still identify concept intent?
- Show inverted (white on dark) → hierarchy maintained?

**Example Error:** Current template emphasizes circuit nodes equally to main gear (should be subtle support)

---

## PRODUCTION DELIVERABLES

For EACH of the 3-5 selected concepts, produce:

### Core Variations (3 required)
1. **Full Color Version**
   - Uses complete color palette (primary + secondary + accent)
   - Tested on white background
   - High contrast, professional appearance
   - File format: .SVG (editable) + .PNG (300 DPI raster)

2. **Monochrome Version**
   - Black (#111111) only, on white background
   - Must retain full visual hierarchy and clarity
   - Essential for: grant applications, letterhead, simple reproduction
   - File format: .SVG + .PNG (300 DPI)

3. **Inverted Version**
   - White on dark background (use #1a1a1a or color background)
   - Maintains contrast and readability
   - Essential for: website headers, dark UI, social media
   - File format: .SVG + .PNG (300 DPI)

### Scale Verification Assets (5 required)
- Single composite image showing logo at all 5 scales (0.5", 1", 2", 6", 24")
- Includes measurement indicators
- Format: .PNG at 300 DPI, minimum 3000px wide

### Context Mockups (4 required)
Demonstrate how logo functions in real-world applications:

1. **Website Header Mockup**
   - Dimensions: 960px wide × 120px tall (typical header height)
   - Include sample navigation and hero imagery
   - Show color and monochrome versions
   - Format: .PNG at 96 DPI (web standard)

2. **Business Card Mockup**
   - Dimensions: 3.5" × 2" (standard US size)
   - Front side: logo + organization name + key info
   - Back side: logo + mission statement + contact
   - Format: .PNG at 300 DPI (print-ready reference)

3. **Social Media Profile Mockup**
   - Dimensions: 1200px × 630px (LinkedIn, Facebook standard)
   - Show logo in context with supporting imagery
   - Demonstrate how it appears in social feeds
   - Format: .PNG at 96 DPI

4. **Event Poster Mockup**
   - Dimensions: 36" × 24" (standard poster size)
   - Large-scale application showing impact and clarity
   - Include sample event information
   - Demonstrate use of multiple colors, typography integration
   - Format: .PNG at 150 DPI

---

## DESIGN REVIEW CHECKLIST

Before finalizing any concept, verify:

### Precision ✅
- [ ] All curves are smooth and mathematically correct (no hand-drawn wobbles)
- [ ] All angles are precise (measure in design tool)
- [ ] Symmetry is verified (use mirror/flip tools to confirm)
- [ ] No stray nodes or paths

### Consistency ✅
- [ ] All stroke widths are intentional and consistent
- [ ] All colors use exact hex codes from palette
- [ ] Typography (if used) matches TYPOGRAPHY_SYSTEM.md standards
- [ ] Spacing/padding is uniform throughout

### Scalability ✅
- [ ] Tested at 0.5" → detail remains clear
- [ ] Tested at 1" → proportions unchanged
- [ ] Tested at 24" → doesn't feel overly simple
- [ ] Monochrome version readable at all scales

### Accessibility ✅
- [ ] WCAG AA contrast met (4.5:1 for text, 3:1 for graphics)
- [ ] Tested in colorblind simulator (Coblis protanopia/deuteranopia)
- [ ] Inverted version maintains contrast
- [ ] No information conveyed by color alone

### Brand Alignment ✅
- [ ] Concept clearly communicates assigned pillar(s)
- [ ] Visual direction matches "Modern + Industrial + Community"
- [ ] Professional enough for grant applications
- [ ] Distinctive and memorable (not generic tech)

### File Organization ✅
- [ ] Master vector file (.AI or .SVG) properly layered
- [ ] All fonts embedded or outlined (no missing font warnings)
- [ ] Export settings documented (300 DPI for print, 96 DPI for web)
- [ ] File naming convention followed: `NN-ConceptName/logo-[variant].svg`

---

## WHAT CONSTITUTES "IMMATURE" DESIGN

Current templates exhibit these production-value gaps:

1. **Geometric Imprecision**
   - Gear teeth angles vary inconsistently
   - Circuit paths lack mathematical consistency
   - Node sizes feel arbitrary, not designed

2. **Visual Hierarchy Issues**
   - Accent nodes (lime) receive equal visual weight to primary gear
   - No clear focal point (equal emphasis everywhere)
   - Monochrome version loses all hierarchy

3. **Scalability Problems**
   - Node dots fixed at 3px → disappear at 0.5"
   - Stroke widths not proportional to design scale
   - Detail level inappropriate for intended use sizes

4. **Technical Execution**
   - SVG paths not optimized (will cause rendering issues in web/print)
   - Inconsistent stroke/fill treatment
   - No opacity/blending considerations

5. **Professional Presentation**
   - No context mockups (can't evaluate real-world use)
   - No monochrome verification (fails grant/print requirements)
   - No scale verification (doesn't prove "works at all sizes" claim)

---

## REVISED PHASE 1 TIMELINE

**What Changes:**
- Feb 1: Concept selection + design tool setup + production brief
- Feb 1-2: HIGH-FIDELITY mockup creation (not template refinement)
- Feb 2-3: Context mockups, scale testing, final polish
- Feb 3 AM: Internal quality review against checklist
- Feb 3 PM: Stakeholder presentation (production-ready designs)

**Effort Implication:**
- Each concept: ~16-20 hours professional design work
- Recommended: Focus on 1-2 concepts at production quality vs. 5 at prototype quality

---

## EXAMPLES FROM BRAND WORLD

### ✅ Production-Quality Tech Logos (Reference)
- **Slack:** Simple geometric mark, tests at all scales, clear in monochrome, perfect curves
- **Dropbox:** Clean geometric shape, works from favicon to billboard, instantly recognizable
- **Tesla:** Bold, simple, sophisticated, highly scalable, memorable

### ❌ Immature Logos (What to Avoid)
- Hand-drawn imprecision disguised as "artistic"
- Overly complex detail that fails at small scales
- Color-dependent readability (fails monochrome requirement)
- Inconsistent geometry suggesting digital sloppiness

---

## APPROVAL GATE

**Production-quality mockups are REQUIRED before Feb 3 stakeholder presentation.**

The Implementation Checklist cannot advance from 🔄 "Concepts in progress" to ✅ "Concepts ready for stakeholder feedback" without:
- [ ] All selected concepts meet Design Review Checklist
- [ ] All scale verification images created and reviewed
- [ ] All 4 context mockups completed
- [ ] Monochrome versions tested and approved
- [ ] @CTO confirms production standards met

**Do not schedule stakeholder meeting until quality gate passed.**

---

## NEXT ACTION FOR @CTO

1. Select 1-2 concepts to develop to production quality (not all 5)
2. Open selected concept template in professional design tool (Adobe Illustrator recommended)
3. Rebuild design from scratch using precision tools, not template adjustment
4. Reference this document's standards for each refinement step
5. Create all required variations and mockups
6. Submit for internal quality review (use checklist)
7. Iterate until production-ready

**Recommended Concepts:**
- **Concept 1 (Gear + Circuit):** Most commercially viable, clear metaphor
- **Concept 3 (Detroit Circuit):** Most unique, strongest brand differentiation

---

**Status:** 🔄 PRODUCTION STANDARDS ESTABLISHED, AWAITING DESIGN EXECUTION

Document created to establish quality expectations and unblock design work.
