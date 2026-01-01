#!/usr/bin/env python3
"""
Tests for Detroit Automation Academy examples
"""

import sys
import os

# Add parent directory to path to allow importing from sibling packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import pytest  # Commented out since pytest may not be installed
from challenges.challenge_1_rover_debug import Rover

def test_rover_initialization():
    rover = Rover(x=5, y=5)
    assert rover.get_position() == (5, 5)
    assert rover.battery == 100
    print("✓ test_rover_initialization passed")

def test_rover_movement():
    # Note: These tests verify the API exists, but the logic inside Rover
    # is intentionally buggy for the challenge.
    rover = Rover(x=0, y=0)
    
    # Test that methods exist and run without crashing
    rover.move_east()
    rover.move_north()
    
    print("✓ test_rover_movement passed")

if __name__ == "__main__":
    print("Running tests...")
    test_rover_initialization()
    test_rover_movement()
    print("All tests passed!")