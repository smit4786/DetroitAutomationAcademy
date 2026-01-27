#!/usr/bin/env python3
"""
Phase 1: Python Fundamentals & Microcontrollers (Raspberry Pi)
Example: LED Blinking Script

This script demonstrates basic GPIO control on a Raspberry Pi.
It blinks an LED connected to GPIO pin 17.
"""

import time

import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pin number
LED_PIN = 17

# Set up the pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)


def blink_led(pin, duration=1.0, times=5):
    """
    Blink an LED connected to the specified pin.

    Args:
        pin (int): GPIO pin number
        duration (float): Duration of each blink in seconds
        times (int): Number of times to blink
    """
    for _ in range(times):
        GPIO.output(pin, GPIO.HIGH)  # Turn LED on
        time.sleep(duration)
        GPIO.output(pin, GPIO.LOW)  # Turn LED off
        time.sleep(duration)


if __name__ == "__main__":
    try:
        print("Blinking LED on pin", LED_PIN)
        blink_led(LED_PIN, 0.5, 10)
        print("Done!")
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
