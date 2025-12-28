# API Documentation

This document provides detailed API documentation for all classes, functions, and modules in the Detroit Automation Academy codebase.

## Module: detroit_automation_academy

Main module containing project description and overview.

**Docstring:** Comprehensive project description including opportunity, solution, program overview, and key outcomes.

---

## Module: phase1.led_blink

### blink_led(pin, duration=1.0, times=5)

Blink an LED connected to the specified GPIO pin.

**Parameters:**
- `pin` (int): GPIO pin number where LED is connected
- `duration` (float): Duration of each blink in seconds (default: 1.0)
- `times` (int): Number of times to blink the LED (default: 5)

**Returns:** None

**Example:**
```python
blink_led(17, 0.5, 10)  # Blink LED on pin 17 for 0.5s, 10 times
```

---

## Module: phase1.button_press

### button_pressed(pin)

Callback function executed when a button press is detected.

**Parameters:**
- `pin` (int): GPIO pin number where button is connected

**Returns:** None

**Notes:** This function is automatically called by GPIO event detection when a falling edge is detected on the specified pin.

---

## Module: phase3.autonomous_rover

### Class: Rover

Represents an autonomous rover with position and orientation in a 2D grid world.

#### Constructor: Rover(x=0, y=0)

**Parameters:**
- `x` (int): Initial x-coordinate (default: 0)
- `y` (int): Initial y-coordinate (default: 0)

#### Methods:

##### move_forward()

Move the rover one unit forward in its current direction.

**Returns:** None

##### turn_left()

Rotate the rover 90 degrees counterclockwise.

**Returns:** None

##### turn_right()

Rotate the rover 90 degrees clockwise.

**Returns:** None

##### get_position()

Get the current position of the rover.

**Returns:** tuple (x, y) - Current coordinates

---

### Class: World

Represents a 2D grid world with obstacles and boundaries.

#### Constructor: World(width=10, height=10)

**Parameters:**
- `width` (int): Width of the world grid (default: 10)
- `height` (int): Height of the world grid (default: 10)

#### Methods:

##### is_valid_position(x, y)

Check if a given position is valid (within bounds and not on obstacle).

**Parameters:**
- `x` (int): X-coordinate to check
- `y` (int): Y-coordinate to check

**Returns:** bool - True if position is valid, False otherwise

##### display(rover)

Display the world as an ASCII grid with rover and obstacles.

**Parameters:**
- `rover` (Rover): The rover object to display

**Returns:** None

**Output:** ASCII grid where:
- 'R' = rover position
- '#' = obstacle
- '.' = empty space

---

### Function: simple_autonomous_navigation(rover, world, steps=20)

Simulate simple autonomous navigation behavior.

**Parameters:**
- `rover` (Rover): The rover object to control
- `world` (World): The world object containing obstacles
- `steps` (int): Number of simulation steps (default: 20)

**Returns:** None

**Behavior:** Attempts to move forward, turns randomly if blocked by obstacles or boundaries.

---

## Module: test_examples

### test_rover_initialization()

Test rover initialization with default and custom positions.

**Returns:** None

### test_rover_movement()

Test rover movement and rotation functionality.

**Returns:** None

### test_world_bounds()

Test world boundary and obstacle checking.

**Returns:** None

---

## Dependencies

### Core Dependencies
- Python 3.8+
- RPi.GPIO (for Raspberry Pi GPIO control)
- numpy (for numerical computations)
- matplotlib (for data visualization)
- pandas (for data manipulation)
- opencv-python (for computer vision)
- dronekit (for drone control)

### Development Dependencies
- pytest (for testing)
- black (for code formatting)
- flake8 (for linting)

### Hardware Dependencies
- Raspberry Pi 4+ (for Phase 1 examples)
- GPIO-connected LEDs and buttons
- Optional: Sensors, motors, cameras

---

## Error Handling

All GPIO operations should be wrapped in try-except blocks:

```python
try:
    # GPIO operations
    pass
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    GPIO.cleanup()  # Always clean up GPIO
```

Common exceptions:
- `RuntimeError`: GPIO access denied (run with sudo)
- `ValueError`: Invalid pin number or mode
- `TypeError`: Incorrect parameter types

---

## Constants

### GPIO Pin Modes
- `GPIO.BCM`: Broadcom pin numbering
- `GPIO.BOARD`: Physical pin numbering

### GPIO States
- `GPIO.HIGH`: Logic high (3.3V)
- `GPIO.LOW`: Logic low (0V)

### GPIO Directions
- `GPIO.OUT`: Output pin
- `GPIO.IN`: Input pin

### Pull Resistor States
- `GPIO.PUD_UP`: Enable internal pull-up resistor
- `GPIO.PUD_DOWN`: Enable internal pull-down resistor

---

## Performance Considerations

- GPIO operations are relatively slow; avoid tight loops
- Use event detection for button inputs instead of polling
- Clean up GPIO resources properly to avoid conflicts
- Consider using PWM for smooth LED brightness control

---

## Security Notes

- GPIO access requires root privileges on Raspberry Pi
- Always validate input parameters to prevent hardware damage
- Use appropriate current-limiting resistors for LEDs
- Implement proper error handling for sensor failures