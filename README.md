# DetroitAutomationAcademy

The Opportunity
Detroit is the global epicenter of mobility innovation, yet a significant disconnect remains
between the advanced technologies being developed at Michigan Central and the educational
opportunities available to Detroit's youth. While software jobs are booming, few programs exist
that bridge the gap between code and physical application. To ensure the next generation of
Detroiters can build, maintain, and innovate within the autonomous sector, we must move
beyond screen-based coding to "Physical Computing."
 
The Solution
Automated Technologies proposes The Detroit Automation Academy, a 24-week immersive
workforce development fellowship hosted at the Youth STEM Lab. Unlike traditional bootcamps,
our curriculum is rooted in industrial application. We teach high school students (Grades 9-12)
how to write Python code that controls the physical world—from autonomous rovers to aerial
drones.
By leveraging Michigan Central's state-of-the-art makerspace, we transform abstract concepts
into tangible skills. Students don't just learn syntax; they 3D print rover chassis, laser-cut sensor
mounts, and write the algorithms that allow these machines to navigate the world autonomously.
Program Overview
• Structure: Two 12-week cohorts (Spring & Fall 2026).
• Capacity: 50 Students total (25 per cohort).
• Target Audience: Detroit residents (Districts 1-5), with a goal of 50% female participation.
• Curriculum:
• Phase 1: Python Fundamentals & Microcontrollers (Raspberry Pi).
• Phase 2: CAD Design & Rapid Prototyping (3D Printing/Laser Cutting).
• Phase 3: Autonomous Systems & Sensor Fusion (Capstone Projects).
Key Outcomes
1. Industrial Fluency: Students gain intermediate proficiency in Python and Linux environments,
the standard toolset for modern robotics.
2. Certification: Graduates earn the Automated Technologies Junior Technologist Certificate and
complete FAA Part 107 (Drone Pilot) prep work.
3. Career Pathways: Direct mentorship from industry practitioners and exposure to the Newlab
ecosystem, demystifying careers in advanced manufacturing and mobility.

## Installation

### Prerequisites
- Python 3.8 or higher
- Raspberry Pi (for Phase 1 hardware examples)
- Git

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/DetroitAutomationAcademy.git
cd DetroitAutomationAcademy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For development, install additional tools:
```bash
pip install -e .
```

## Project Structure

```
DetroitAutomationAcademy/
├── README.md                    # Project overview and documentation
├── pyproject.toml              # Python packaging configuration
├── requirements.txt            # Python dependencies
├── detroit_automation_academy.py # Main module with project description
├── phase1/                     # Python Fundamentals & Microcontrollers
│   ├── led_blink.py           # GPIO output example
│   └── button_press.py        # GPIO input example
├── phase2/                     # CAD Design & Rapid Prototyping
│   └── cad_design.py          # 3D model and G-code generation
├── phase3/                     # Autonomous Systems & Sensor Fusion
│   └── autonomous_rover.py    # Navigation simulation
├── docs/                       # Documentation
│   ├── quick_start.md         # Getting started guide
│   ├── api_reference.md       # API documentation
│   ├── phase1_guide.md        # Phase 1 detailed guide
│   └── phase3_guide.md        # Phase 3 detailed guide
└── test_examples.py           # Unit tests
```

## Documentation

- **[Quick Start Guide](docs/quick_start.md)** - Get up and running quickly
- **[API Reference](docs/api_reference.md)** - Detailed API documentation
- **[Phase 1 Guide](docs/phase1_guide.md)** - Python fundamentals & microcontrollers
- **[Phase 3 Guide](docs/phase3_guide.md)** - Autonomous systems & sensor fusion

## Examples

### Phase 1: Hardware Examples (Raspberry Pi)
```bash
# LED Blinking
sudo python3 phase1/led_blink.py

# Button Press Detection
sudo python3 phase1/button_press.py
```

### Phase 2: CAD Design Examples
```bash
# Generate 3D models and G-code
python3 phase2/cad_design.py
```

### Phase 3: Simulation Examples
```bash
# Autonomous Rover
python3 phase3/autonomous_rover.py
```

### Testing
```bash
python3 test_examples.py
```

## Curriculum Phases

### Phase 1: Python Fundamentals & Microcontrollers
Focuses on basic Python programming and Raspberry Pi GPIO control.

**Examples:**
- LED control and blinking patterns
- Button input and event handling
- Basic sensor integration

### Phase 2: CAD Design & Rapid Prototyping
Introduces computer-aided design and physical prototyping.

**Examples:**
- Parametric 3D model generation (STL files)
- Laser cutting path optimization (G-code)
- 3D printing preparation scripts

### Phase 3: Autonomous Systems & Sensor Fusion
Advanced topics in robotics and autonomous navigation.

**Examples:**
- Grid-based pathfinding algorithms
- Sensor data fusion techniques
- Computer vision for obstacle detection

## Development

### Code Style
This project uses:
- Black for code formatting
- Flake8 for linting
- Type hints where appropriate

### Testing
Run tests with:
```bash
python3 test_examples.py
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Hardware Requirements

### Phase 1 Setup
- Raspberry Pi 4 or newer
- Breadboard and jumper wires
- LEDs, resistors, and push buttons
- Optional: Sensors (temperature, distance, etc.)

### Phase 2 Setup
- 3D printer (e.g., Ender 3)
- Laser cutter
- CAD software (FreeCAD, Fusion 360)

### Phase 3 Setup
- Camera module for computer vision
- Additional sensors for autonomous navigation
- Motor controllers for robot movement

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions about the Detroit Automation Academy program, contact:
- Email: dbkrsmith@gmail.com

## Acknowledgments

- Michigan Central for providing the makerspace
- Youth STEM Lab for hosting facilities
- Newlab for industry mentorship opportunities
