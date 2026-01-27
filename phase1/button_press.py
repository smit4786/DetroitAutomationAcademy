#!/usr/bin/env python3
"""
Phase 1: Python Fundamentals & Microcontrollers (Raspberry Pi)
Example: Button Press Detection

This script demonstrates reading input from a button connected to GPIO pin 18.
It prints a message when the button is pressed.
"""

import time

import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pin numbers
BUTTON_PIN = 18

# Set up the pin as an input with pull-up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def button_pressed(pin):
    """
    Callback function called when button is pressed.

    Args:
        pin (int): GPIO pin number
    """
    print("Button pressed on pin", pin)


# Add event detection for button press (falling edge)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed, bouncetime=200)

if __name__ == "__main__":
    try:
        print("Waiting for button press on pin", BUTTON_PIN)
        print("Press Ctrl+C to exit")
        while True:
            time.sleep(1)  # Keep the program running
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
