# Phase 2: CAD Design & Rapid Prototyping

This phase introduces students to computer-aided design (CAD) and rapid prototyping techniques using 3D printing and laser cutting.

## Learning Objectives

By the end of Phase 2, students will be able to:
- Create parametric 3D models using Python
- Generate STL files for 3D printing
- Produce G-code for laser cutting
- Understand CAD design principles
- Apply rapid prototyping in robotics projects

## Software and Tools

### Required Software
- Python 3.8+ (for CAD script execution)
- 3D printing software (Cura, PrusaSlicer, or similar)
- Laser cutting software (compatible with G-code)
- STL file viewer (optional: FreeCAD, Meshlab)

### Hardware Requirements
- 3D printer (FDM type recommended for beginners)
- Laser cutter (with G-code support)
- Computer for design and slicing

## CAD Design Fundamentals

### Parametric Design
Parametric design means creating models where dimensions and features are defined by parameters that can be easily changed.

**Advantages:**
- Easy to modify designs
- Consistent scaling
- Automated generation of variations
- Integration with programming

### 3D Model Formats
- **STL (STereoLithography)**: Most common format for 3D printing
- **OBJ**: Alternative format with material support
- **STEP/IGES**: Professional CAD formats (more complex)

### Coordinate Systems
- **Right-hand rule**: X (right), Y (forward), Z (up)
- **Origin**: (0,0,0) is typically the center or corner of the model
- **Units**: Millimeters for most 3D printing applications

## 3D Printing Basics

### FDM (Fused Deposition Modeling) Process
1. **Design**: Create 3D model
2. **Slice**: Convert to G-code with slicing software
3. **Print**: Extrude melted plastic layer by layer

### Key Parameters
- **Layer Height**: 0.1-0.3mm (finer = smoother but slower)
- **Infill**: 10-30% for most functional parts
- **Wall Thickness**: 2-4 shells for strength
- **Supports**: Required for overhangs >45°

### Common Materials
- **PLA**: Easy to print, biodegradable, good for prototyping
- **PETG**: Durable, temperature resistant, good for functional parts
- **ABS**: Strong, heat resistant, requires heated bed

### Print Settings by Material

| Material | Bed Temp (°C) | Nozzle Temp (°C) | Print Speed (mm/s) |
|----------|---------------|------------------|-------------------|
| PLA      | 50-60        | 190-220         | 50-80            |
| PETG     | 70-80        | 220-250         | 40-60            |
| ABS      | 90-110       | 220-250         | 40-60            |

## Laser Cutting Basics

### Process Overview
Laser cutting uses a focused laser beam to vaporize material, creating precise cuts.

### Materials
- **Wood**: Plywood, MDF (3-6mm thickness)
- **Acrylic**: Cast and extruded (3-10mm)
- **Cardboard**: For prototyping
- **Paper**: For templates and patterns

### G-code for Laser Cutting
- **G0**: Rapid movement (laser off)
- **G1**: Linear cutting (laser on)
- **M3**: Laser on (spindle clockwise)
- **M5**: Laser off (spindle stop)
- **S###**: Laser power setting

## CAD Design Script (`cad_design.py`)

The provided script demonstrates parametric CAD generation using pure Python.

### STLWriter Class

**Purpose:** Generate STL files for 3D printing

**Key Methods:**
```python
stl = STLWriter('model.stl')  # Create STL writer
stl.add_triangle(v1, v2, v3)   # Add triangle with vertices
stl.write()                    # Save to file
```

**Triangle Format:**
- Vertices defined as (x, y, z) tuples
- Normal vector calculated automatically
- Counter-clockwise winding for correct orientation

### 3D Model Generation

#### Rover Chassis (`create_rover_chassis()`)
Creates a rectangular box chassis for robotic vehicles.

**Parameters:**
- `width`: Chassis width (default: 12mm)
- `height`: Chassis height (default: 6mm)
- `length`: Chassis length (default: 18mm)

**Features:**
- Solid rectangular structure
- Mounting points for components
- Lightweight design with internal space

#### Sensor Mount (`create_sensor_mount()`)
Creates a cylindrical mount for sensors or cameras.

**Parameters:**
- `radius`: Cylinder radius (default: 3mm)
- `height`: Cylinder height (default: 4mm)

**Features:**
- Cylindrical body for rotation
- Mounting holes for screws
- Smooth surface for sensor attachment

### Laser Cutting G-code Generation

#### G-code Structure
```
; Header comments
G21 ; Set units to millimeters
G90 ; Absolute positioning
M3 S255 ; Laser on at full power
G0 X0 Y0 ; Move to start position
G1 Z-1 F100 ; Lower to cutting depth
; Cutting paths...
G0 Z5 ; Raise to safe height
M5 ; Laser off
G0 X0 Y0 ; Return to origin
M30 ; End program
```

#### Shape Generation
- **Square**: Simple rectangular cuts
- **Circle**: Approximated with G2/G3 arc commands
- **Triangle**: Linear cuts between vertices

## Examples and Exercises

### Exercise 1: Custom Chassis Design
```python
# Modify chassis dimensions
create_rover_chassis(width=15, height=8, length=20)
```

**Tasks:**
- Change dimensions and observe STL file
- Add mounting holes
- Create different chassis shapes

### Exercise 2: Sensor Array
```python
# Create multiple sensor mounts
for i in range(3):
    create_sensor_mount(radius=2+i*0.5, height=3+i)
```

**Tasks:**
- Arrange mounts in a line
- Create different sizes for various sensors
- Add connecting structures

### Exercise 3: Laser Cut Patterns
```python
# Generate custom cutting patterns
generate_gcode_for_laser_cutting("square", 20)
generate_gcode_for_laser_cutting("triangle", 15)
```

**Tasks:**
- Create custom shapes (hexagon, star)
- Add engraving patterns
- Design interlocking parts

## 3D Printing Workflow

### 1. Design Phase
```bash
# Generate STL model
python3 phase2/cad_design.py
```

### 2. Slicing Phase
1. Open STL in slicing software (Cura, PrusaSlicer)
2. Select material and quality settings
3. Add supports if needed
4. Generate G-code

### 3. Printing Phase
1. Load filament matching material type
2. Level build plate
3. Start print job
4. Monitor first few layers

### 4. Post-Processing
- Remove supports
- Sand rough surfaces
- Test fit with other components

## Laser Cutting Workflow

### 1. Design Phase
```bash
# Generate G-code
python3 phase2/cad_design.py
```

### 2. Material Preparation
- Select appropriate material thickness
- Ensure material is flat and secure
- Set correct focus distance

### 3. Cutting Phase
1. Load G-code into laser software
2. Set power and speed parameters
3. Position material correctly
4. Execute cut

### 4. Finishing
- Remove cut pieces
- Clean edges if needed
- Test assembly fit

## Troubleshooting

### 3D Printing Issues

1. **Poor Layer Adhesion**
   - Check bed leveling
   - Increase bed temperature
   - Clean build surface

2. **Stringing/Oozing**
   - Reduce print temperature
   - Increase retraction settings
   - Slow down print speed

3. **Warping**
   - Use brim or raft
   - Increase bed temperature
   - Improve bed adhesion

4. **Layer Shifting**
   - Check belt tension
   - Clean linear rails
   - Reduce acceleration settings

### Laser Cutting Issues

1. **Incomplete Cuts**
   - Increase laser power
   - Decrease cutting speed
   - Check focus alignment

2. **Burning/Excessive Heat**
   - Reduce laser power
   - Increase cutting speed
   - Use air assist if available

3. **Inaccurate Cuts**
   - Check calibration
   - Verify G-code coordinates
   - Ensure material is flat

### CAD Script Issues

1. **Invalid STL Files**
   - Check triangle winding order
   - Verify vertex coordinates
   - Ensure closed mesh

2. **G-code Errors**
   - Validate coordinate ranges
   - Check laser power settings
   - Verify movement commands

## Advanced Topics

### Mesh Optimization
- Reduce triangle count for faster printing
- Ensure manifold geometry (no holes)
- Optimize for print orientation

### Multi-part Assemblies
- Design interlocking features
- Include alignment pins
- Plan assembly sequence

### Material Selection
- Consider strength requirements
- Think about temperature resistance
- Factor in cost and availability

## Integration with Robotics

### Mounting Considerations
- Design for sensor alignment
- Include cable management
- Plan for component access

### Tolerance Design
- Account for 3D printing tolerances (±0.1-0.2mm)
- Design for press-fit assemblies
- Include adjustment features

### Iterative Design
- Print, test, modify, repeat
- Start with simple prototypes
- Refine based on testing results

## Resources

- [3D Printing Basics](https://www.simplify3d.com/support/print-quality-troubleshooting/)
- [G-code Reference](https://marlinfw.org/meta/gcode/)
- [STL File Format](https://en.wikipedia.org/wiki/STL_(file_format))
- [FreeCAD Documentation](https://wiki.freecadweb.org/)
- [Cura Slicing Software](https://ultimaker.com/software/ultimaker-cura)

## Safety Guidelines

### 3D Printing Safety
- **Ventilation**: Print in well-ventilated area (some filaments emit fumes)
- **Temperature**: Hot surfaces can cause burns
- **Moving Parts**: Keep hands clear of printer mechanisms
- **Power**: Unplug when not in use

### Laser Cutting Safety
- **Eye Protection**: Always wear laser safety goggles
- **Fire Prevention**: Keep fire extinguisher nearby
- **Material Safety**: Some materials produce toxic fumes when cut
- **Supervision**: Never leave laser unattended

### General Lab Safety
- **Tool Usage**: Use tools properly and safely
- **Cleanup**: Keep workspace organized
- **Emergency**: Know location of first aid kit and emergency exits