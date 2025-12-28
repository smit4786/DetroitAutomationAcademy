#!/usr/bin/env python3
"""
Phase 3: Autonomous Systems & Sensor Fusion (Capstone Projects)
Example: Simple Autonomous Rover Simulation

This script simulates a basic autonomous rover that navigates a simple grid world.
It demonstrates basic pathfinding and obstacle avoidance concepts.
"""

import random
import time

class Rover:
    """
    Represents an autonomous rover with position and orientation.

    The rover can move in a 2D grid world and rotate in 90-degree increments.
    Direction mapping: 0=North, 1=East, 2=South, 3=West
    """

    def __init__(self, x=0, y=0):
        """
        Initialize the rover at a given position.

        Args:
            x (int): Initial x-coordinate (default: 0)
            y (int): Initial y-coordinate (default: 0)
        """
        self.x = x
        self.y = y
        self.direction = 0  # 0: North, 1: East, 2: South, 3: West

    def move_forward(self):
        """
        Move the rover one unit forward in its current direction.
        Updates the x or y coordinate based on current direction.
        """
        if self.direction == 0:      # North
            self.y += 1
        elif self.direction == 1:    # East
            self.x += 1
        elif self.direction == 2:    # South
            self.y -= 1
        elif self.direction == 3:    # West
            self.x -= 1

    def turn_left(self):
        """
        Rotate the rover 90 degrees counterclockwise.
        Direction wraps around from 0 to 3.
        """
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        """
        Rotate the rover 90 degrees clockwise.
        Direction wraps around from 3 to 0.
        """
        self.direction = (self.direction + 1) % 4

    def get_position(self):
        """
        Get the current position of the rover.

        Returns:
            tuple: (x, y) coordinates of the rover
        """
        return (self.x, self.y)

class World:
    """
    Represents a 2D grid world with obstacles and boundaries.

    The world has defined width and height, and contains randomly placed obstacles.
    Rovers can only move to valid positions within bounds and not on obstacles.
    """

    def __init__(self, width=10, height=10):
        """
        Initialize the world with given dimensions and random obstacles.

        Args:
            width (int): Width of the world grid (default: 10)
            height (int): Height of the world grid (default: 10)
        """
        self.width = width
        self.height = height
        self.obstacles = set()
        # Add some random obstacles
        for _ in range(5):
            self.obstacles.add((random.randint(0, width-1), random.randint(0, height-1)))

    def is_valid_position(self, x, y):
        """
        Check if a given position is valid (within bounds and not on obstacle).

        Args:
            x (int): X-coordinate to check
            y (int): Y-coordinate to check

        Returns:
            bool: True if position is valid, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

    def display(self, rover):
        """
        Display the world as an ASCII grid with rover and obstacles.

        Args:
            rover (Rover): The rover to display in the world

        Prints:
            ASCII representation where:
            - 'R' represents the rover
            - '#' represents obstacles
            - '.' represents empty space
        """
        for y in range(self.height-1, -1, -1):
            for x in range(self.width):
                if (x, y) == rover.get_position():
                    print('R', end='')
                elif (x, y) in self.obstacles:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()

def simple_autonomous_navigation(rover, world, steps=20):
    """
    Simple autonomous navigation: move forward if possible, otherwise turn randomly.

    Args:
        rover (Rover): The rover object
        world (World): The world object
        steps (int): Number of steps to simulate
    """
    for step in range(steps):
        print(f"Step {step + 1}:")
        world.display(rover)

        # Try to move forward
        original_pos = rover.get_position()
        rover.move_forward()
        if not world.is_valid_position(rover.x, rover.y):
            # Hit obstacle or boundary, go back and turn
            rover.x, rover.y = original_pos
            if random.choice([True, False]):
                rover.turn_left()
            else:
                rover.turn_right()

        time.sleep(0.5)  # Slow down for visualization

if __name__ == "__main__":
    rover = Rover(0, 0)
    world = World(10, 10)
    print("Starting autonomous rover simulation...")
    simple_autonomous_navigation(rover, world, 20)
    print("Simulation complete!")