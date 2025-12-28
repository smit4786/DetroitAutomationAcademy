# Phase 1: Python Fundamentals & Microcontrollers

This phase introduces students to Python programming and basic microcontroller interaction using the Raspberry Pi.

## Learning Objectives

By the end of Phase 1, students will be able to:
- Write basic Python scripts
- Control GPIO pins on a Raspberry Pi
- Read input from sensors and buttons
- Implement basic control loops
- Debug hardware-software interactions

## Hardware Setup

### Required Components
- Raspberry Pi 4 or newer
- Breadboard
- Jumper wires (male-to-male, male-to-female)
- LEDs (various colors)
- 220Ω resistors
- Push buttons
- Optional: Temperature sensor (DS18B20), ultrasonic distance sensor

### GPIO Pin Layout
```
Raspberry Pi GPIO Layout:
3V3  (1) (2)  5V
GPIO2 (3) (4)  5V
GPIO3 (5) (6)  GND
GPIO4 (7) (8)  GPIO14
GND   (9) (10) GPIO15
GPIO17(11)(12) GPIO18
GPIO27(13)(14) GND
GPIO22(15)(16) GPIO23
3V3  (17)(18) GPIO24
GPIO10(19)(20) GND
GPIO9 (21)(22) GPIO25
GPIO11(23)(24) GPIO8
GND  (25)(26) GPIO7
GPIO0 (27)(28) GPIO1
GPIO5 (29)(30) GND
GPIO6 (31)(32) GPIO12
GPIO13(33)(34) GND
GPIO19(35)(36) GPIO16
GPIO26(37)(38) GPIO20
GND  (39)(40) GPIO21
```

## Examples

### LED Blinking (`led_blink.py`)

This example demonstrates basic GPIO output control.

**Circuit Setup:**
- Connect LED anode (+) to GPIO pin 17 through a 220Ω resistor
- Connect LED cathode (-) to GND

**Code Explanation:**
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(17, GPIO.OUT)  # Set pin 17 as output

GPIO.output(17, GPIO.HIGH)  # Turn LED on
time.sleep(1)  # Wait 1 second
GPIO.output(17, GPIO.LOW)   # Turn LED off

GPIO.cleanup()  # Clean up GPIO settings
```

### Button Press Detection (`button_press.py`)

This example shows how to read digital input from a button.

**Circuit Setup:**
- Connect one button pin to GPIO pin 18
- Connect the other button pin to GND
- Enable internal pull-up resistor in software

**Code Explanation:**
```python
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=button_callback)
```

## Exercises

1. **Traffic Light Controller**
   - Control 3 LEDs (red, yellow, green) to simulate a traffic light
   - Implement timing for each state

2. **Binary Counter**
   - Use multiple LEDs to display binary numbers
   - Increment counter with button press

3. **Temperature Monitor**
   - Read temperature from DS18B20 sensor
   - Display temperature on console
   - Turn on LED if temperature exceeds threshold

4. **Distance Sensor**
   - Use ultrasonic sensor to measure distance
   - Display distance readings
   - Sound alarm (LED) when object is too close

## Troubleshooting

### Common Issues

1. **Permission Denied Error**
   - GPIO access requires root privileges
   - Run with `sudo python3 script.py`

2. **Channel Already in Use**
   - Previous program didn't clean up GPIO
   - Always call `GPIO.cleanup()` at the end

3. **LED Not Lighting**
   - Check circuit connections
   - Verify correct pin numbers
   - Check resistor value

4. **Button Not Responding**
   - Check button wiring
   - Verify pull-up/down resistor configuration
   - Check for switch bounce (use bouncetime parameter)

### Debugging Tips

- Use `GPIO.input(pin)` to read current pin state
- Add print statements to verify code execution
- Use multimeter to test circuit continuity
- Check Raspberry Pi pinout diagram carefully

## Resources

- [Raspberry Pi GPIO Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)
- [Python GPIO Library](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
- [Adafruit GPIO Tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup)