#!/usr/bin/env python3
"""
Tests for Detroit Automation Academy examples
"""

# import pytest  # Commented out since pytest may not be installed
from phase3.autonomous_rover import Rover, World

def test_rover_initialization():
    rover = Rover(5, 5)
    assert rover.get_position() == (5, 5)
    assert rover.direction == 0
    print("✓ test_rover_initialization passed")

def test_rover_movement():
    rover = Rover(0, 0)
    rover.move_forward()
    assert rover.get_position() == (0, 1)

    rover.turn_right()
    rover.move_forward()
    assert rover.get_position() == (1, 1)
    print("✓ test_rover_movement passed")

def test_world_bounds():
    world = World(5, 5)
    assert world.is_valid_position(0, 0) == True
    assert world.is_valid_position(5, 5) == False
    assert world.is_valid_position(-1, 0) == False
    print("✓ test_world_bounds passed")

if __name__ == "__main__":
    print("Running tests...")
    test_rover_initialization()
    test_rover_movement()
    test_world_bounds()
    print("All tests passed!")