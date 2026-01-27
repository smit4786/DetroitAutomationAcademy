# Copilot Instructions for Detroit Automation Academy

## Project Overview

Detroit Automation Academy is an **educational robotics and automation curriculum** organized in three progressive phases: Python fundamentals with microcontrollers (Phase 1), CAD design and rapid prototyping (Phase 2), and autonomous systems with sensor fusion (Phase 3). The repository contains learning materials, example code, and debugging challenges for students.

## Architecture & Directory Structure

- **`phase1/`**: GPIO control fundamentals (Raspberry Pi, LEDs, buttons) using `RPi.GPIO`
- **`phase2/`**: CAD design with parametric Python models, G-code generation, and STL output
- **`phase3/`**: Autonomous rover simulation with navigation algorithms and sensor concepts
- **`docs/`**: Phase-specific guides, design documents, and architecture references
- **`activations/`**: G-code files for laser cutting demonstration projects

## Key Patterns & Conventions

### Class-Based Simulations
Core simulation classes (`Rover`, `World`) use direction mapping as cardinal integers (0=North, 1=East, 2=South, 3=West). Methods like `turn_left()` and `turn_right()` perform modulo operations on direction values. Always preserve this convention when extending rover behavior. Example: [phase3/autonomous_rover.py](phase3/autonomous_rover.py#L14-L55)

### Debugging Challenges (Pedagogical, Not Defects)
Files like [challenge_1_rover_debug.py](challenge_1_rover_debug.py) intentionally contain bugs (marked with `TODO` comments) for student debugging practice. These are **not defects to fix** but core pedagogical tools—preserve bugs exactly as-is and add similar patterns for new challenges. Each bug teaches a specific lesson:
- **Coordinate system inversions**: e.g., North moves `+y` not `-y` (line 32)
- **Swapped return values**: e.g., returning `(y, x)` instead of `(x, y)` (line 50)
- **Inverted control logic**: e.g., `turn_left()` incorrectly using `+1` instead of `-1` (line 42)
- **Resource management**: e.g., battery increasing instead of decreasing (line 37)

When adding new challenges, follow the pattern: clear docstring explaining the bug domain, TODO comment above each buggy line, and a matching correct implementation in the corresponding phase file for reference.

### Documentation Structure
Each phase has detailed markdown guides in `docs/` with hardware specifications, learning objectives, and algorithm walkthroughs. Keep documentation synchronized with corresponding code examples.

## Dependencies & Development

**Core Dependencies** (from `pyproject.toml`):
- `RPi.GPIO`: Raspberry Pi GPIO control (Phase 1)
- `numpy`, `matplotlib`, `pandas`: Sensor data analysis
- `opencv-python`: Computer vision for autonomous systems
- `dronekit`: Future drone integration
- `pytest`, `black`, `flake8`: Testing and formatting

**Python Version**: Supports 3.8–3.11

**Code Quality**: Enforce Black formatting (88 char line length) and Flake8 linting. No special configuration needed—tools are pre-configured in `pyproject.toml`.

## Critical Workflows

### Running Examples
- **Phase 1 LED blink**: Requires Raspberry Pi hardware or GPIO simulator
- **Phase 2 CAD/G-code generation**: Pure Python with parametric modeling; generates `.stl` (3D print) and `.gcode` (laser cut) files
- **Phase 3 rover simulation**: Pure Python; runs on any platform without external dependencies
- **Debugging challenges**: Import and instantiate the buggy class, then trace expected vs. actual behavior

### Phase 2 G-code Generation Pattern
G-code files in `activations/` are generated from parametric Python models in [phase2/cad_design.py](phase2/cad_design.py). The pattern:
1. **Parametric geometry**: Python functions generate shapes with configurable dimensions (e.g., `laser_cut_circle(radius, precision)`)
2. **G-code output**: Convert paths to linearized G-code with move commands (`G0`, `G1`) and laser control (`M3` on, `M5` off)
3. **Laser-specific settings**: Include power/speed parameters as comments for Epilog Laser Fusion Maker (30-40W CO2, 610×305mm work area)
4. **File naming**: Use descriptive names (`laser_cut_circle.gcode`, `sensor_mount.stl`) matching the part purpose

Example workflow: `cad_design.py` → generates `laser_cut_circle.gcode` → students load into Epilog software → cut acrylic/wood

### Testing
Run tests with: `pytest test_examples.py`

### Code Formatting
Format with: `black <file.py>` or `black .` for entire project

## Integration Points

- **GitHub Actions**: CI/CD pipelines mentioned in curriculum but not yet integrated into this repo
- **Jupyter Lab**: Used in Phase 1 curriculum (referenced in lab-environment README)
- **Docker/Vagrant**: Virtual lab infrastructure housed in separate `daa-lab-environment` repo (Docker Compose with Python, PostgreSQL, Jenkins)
- **Hardware**: Physical tests require Raspberry Pi 4+ with GPIO access; simulations are hardware-agnostic
- **Rapid Prototyping Hardware**: Phase 2 outputs target Bambu Lab (X1 Carbon, A1) for 3D printing and Epilog Laser Fusion Maker (30-40W CO2) for laser cutting

## Adding New Content

1. **New Phase Features**: Add to appropriate `phaseN/` folder with docstrings following Phase 3 rover example style
2. **New Debugging Challenges**: Create file with `TODO` comments marking bugs, similar to [challenge_1_rover_debug.py](challenge_1_rover_debug.py#L29-L45)
3. **Documentation**: Update corresponding guide in `docs/` with learning objectives and hardware requirements
4. **G-code Assets**: Store laser cutting/3D print files in `activations/` with descriptive names

## Avoid Common Mistakes

- Don't remove `TODO` comments from challenge files—they're intentional and mark the exact location of pedagogical bugs
- Direction logic (0-3 mapping) must be consistent across all rover implementations
- GPIO examples are Raspberry Pi–specific; clearly comment platform assumptions
- G-code files must include descriptive comments for laser/printer settings (power, speed, material type)
- Always generate both parametric Python source and exported G-code/STL files; don't ship only binary outputs
