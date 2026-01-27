# Activations

This directory contains G-code files and workflows for community activation events (e.g., Boys & Girls Club demonstrations). Students design parametric shapes in Python, generate G-code, and execute them on the Epilog Laser Fusion Maker.

## Overview

**Learning Objectives:**
- Understand how Python parametric models translate to machine-executable code
- Execute real-world manufacturing processes (laser cutting)
- Connect design decisions to physical outcomes
- Practice CAD-to-production workflows

## Laser Cutting Assets

All files are optimized for the **Epilog Laser Fusion Maker** (30-40W CO2, 610×305mm work area).

### laser_cut_circle.gcode
**Purpose:** Introduces circular geometry and arc movements (G2/G3 commands)

**Learning Focus:**
- Understanding arc commands in G-code
- Circular symmetry and radius calculations
- Material considerations for round cuts

**Recommended Materials:**
- Acrylic (3-5mm): Cuts cleanly, excellent for first-time cuts
- Plywood (3-4mm): Educational, shows wood grain burns
- Cardboard (3-5mm): Budget-friendly, good for prototyping

**Power/Speed Settings:**
- **Acrylic 3mm**: Power 255 (100%), Speed 200 mm/min, ~45 seconds
- **Plywood 3mm**: Power 255, Speed 180 mm/min, ~60 seconds
- **Cardboard 3mm**: Power 200 (80%), Speed 200 mm/min, ~30 seconds

**Estimated Dimensions:** 10mm radius circle at origin

**Generated From:** [phase2/cad_design.py](../phase2/cad_design.py) — `laser_cut_circle()` function

---

### laser_cut_square.gcode
**Purpose:** Introduces linear cutting, corner precision, and material edge quality

**Learning Focus:**
- Straight-line G-code sequences (G1 commands)
- Understanding feed rates and their effect on edge quality
- Debugging sharp corners and dimensional accuracy

**Recommended Materials:**
- Acrylic (3-5mm): Produces frosted edges; best for demonstration
- Wood (2-3mm): Shows precision through burn marks
- Leather (2-3mm): Produces clean cuts with minimal burn

**Power/Speed Settings:**
- **Acrylic 3mm**: Power 255, Speed 200 mm/min, ~40 seconds
- **Wood 2mm**: Power 240 (95%), Speed 150 mm/min, ~50 seconds
- **Leather 3mm**: Power 180 (70%), Speed 220 mm/min, ~35 seconds

**Estimated Dimensions:** 15mm × 15mm square at origin

**Generated From:** [phase2/cad_design.py](../phase2/cad_design.py) — `laser_cut_square()` function

---

### laser_cut_triangle.gcode
**Purpose:** Combines linear and diagonal cuts; introduces trigonometric geometry in CAD

**Learning Focus:**
- Multi-angle cutting strategies
- Rotational geometry and vertex calculations
- Handling non-axis-aligned edges

**Recommended Materials:**
- Acrylic (3-5mm): Best for angular precision
- Cardboard (5mm): Good for exploring kerf (cut width)
- Veneer (1-2mm): Delicate, teaches precision cutting

**Power/Speed Settings:**
- **Acrylic 3mm**: Power 255, Speed 200 mm/min, ~40 seconds
- **Cardboard 5mm**: Power 220 (86%), Speed 180 mm/min, ~50 seconds
- **Veneer 2mm**: Power 150 (59%), Speed 200 mm/min, ~30 seconds

**Estimated Dimensions:** Equilateral triangle, ~12mm base at origin

**Generated From:** [phase2/cad_design.py](../phase2/cad_design.py) — `laser_cut_triangle()` function

---

## Event Workflow: Design-to-Cut (1-2 hours)

1. **Introduction (10 min)**
   - Show finished laser-cut samples
   - Explain Python → G-code → laser connection
   - Demonstrate safe laser operation

2. **Design Phase (20-30 min)**
   - Students customize shape parameters in Python (radius, dimensions, material)
   - Run `cad_design.py` to generate custom G-code
   - Review generated coordinates before cutting

3. **File Preparation (5 min)**
   - Export G-code file with descriptive name (e.g., `student_name_circle.gcode`)
   - Verify file size and command count (prevents runaway programs)

4. **Laser Setup (5 min)**
   - Place material on Epilog bed with alignment marks
   - Load G-code into Epilog software
   - Set material-specific power/speed (see table above)
   - Run air-assist to clear smoke

5. **Cutting (5-10 min per file)**
   - Execute cut with instructor supervision
   - Monitor for smoke/flames
   - Allow cooling before removal (acrylic: 30 sec, wood: 1 min)

6. **Reflection (10 min)**
   - Compare design intent vs. physical result
   - Discuss edge quality, kerf, and material behavior
   - Troubleshoot any issues

---

## Safety Guidelines for Instructors

**Pre-Event Checklist:**
- [ ] Epilog exhaust system is ON and clear of blockages
- [ ] Water cooling system running (watch for low water alarm)
- [ ] Air-assist compressor is functional
- [ ] CO₂ laser tube shows purple/blue glow (not red)
- [ ] Emergency stop button is accessible and tested
- [ ] All mirrors and lenses are clean (use compressed air, not cloth)
- [ ] Material clamps are secure; no protruding edges

**During Cutting:**
- [ ] All students wear laser safety glasses (Class 4)
- [ ] Instructor remains at machine control during operation
- [ ] Lid must be closed during laser firing
- [ ] Never disable interlocks or air-assist
- [ ] Watch for excessive smoke (sign of material ignition)
- [ ] If fire occurs: STOP laser, use CO₂ extinguisher (never water), evacuate if needed

**Post-Event:**
- [ ] Allow material to cool before touching
- [ ] Epilog is powered off
- [ ] Exhaust system runs for 10 minutes after last cut
- [ ] Check bed for debris; clean grates
- [ ] Log cut times and any equipment issues

**Material-Specific Warnings:**
- **Acrylic**: May crack if cut too slowly (low speed) or overheated; water cooling helps
- **Wood**: High fire risk; charring normal but black burn marks indicate too much power
- **Leather**: Real leather only; avoid synthetics (PU, vinyl) as they release toxic fumes
- **Cardboard**: Fire hazard; keep away from cardboard edges with M3 laser on

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Material doesn't cut through | Power too low, speed too fast, or material too thick | Reduce speed 10%, increase power 5%, or thin material |
| Jagged/melted edges | Power too high or speed too slow | Reduce power 5%, increase speed 10% |
| File won't load into Epilog software | G-code syntax error or unsupported command | Regenerate from `cad_design.py`, verify G21/G90 at start |
| Laser fires but doesn't cut | Lens/mirror misalignment or water cooling off | Check water level, run alignment pattern, call Epilog support |
| Smoke/flames during cut | Material catching fire or excessive power | STOP immediately, check material type, reduce power to 70% |

---

## Python Source Integration

To generate custom G-code files for student designs:

```bash
cd phase2
python cad_design.py --shape circle --radius 8 --output ../activations/student_circle.gcode
```

See [phase2/cad_design.py](../phase2/cad_design.py) for parameter options and custom shape support.