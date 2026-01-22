#!/usr/bin/env python3
"""
Challenge 1: Debugging the Rover

This file contains a Rover class with several intentional bugs.
Your task is to identify and fix the logic errors in movement, rotation, and state reporting.
"""

class Rover:
    """
    Represents a rover that navigates a 2D grid.
    
    Directions:
    0: North
    1: East
    2: South
    3: West
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = 0  # Start facing North
        self.battery = 100

    def move_forward(self):
        """
        Move the rover one unit forward in its current direction.
        """
        # TODO: Something feels wrong with the Y-axis movement...
        if self.direction == 0:      # North
            self.y -= 1              # BUG: Should be += 1
        elif self.direction == 1:    # East
            self.x += 1
        elif self.direction == 2:    # South
            self.y += 1              # BUG: Should be -= 1
        elif self.direction == 3:    # West
            self.x -= 1
            
        # TODO: Why does the battery last forever?
        self.battery += 1            # BUG: Should be -= 1

    def turn_left(self):
        """
        Rotate the rover 90 degrees counter-clockwise.
        """
        # TODO: Does this actually turn left?
        self.direction = (self.direction + 1) % 4  # BUG: Turns right

    def turn_right(self):
        """
        Rotate the rover 90 degrees clockwise.
        """
        self.direction = (self.direction + 1) % 4

    def get_position(self):
        """
        Return the current position.
        """
        # TODO: Coordinates seem swapped in the output
        return (self.y, self.x)      # BUG: Returns (y, x) instead of (x, y)

    def get_status(self):
        return f"Rover at ({self.x}, {self.y}) facing {self.direction} with {self.battery}% battery"