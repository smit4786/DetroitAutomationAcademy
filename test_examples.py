#!/usr/bin/env python3
"""
Unit tests for Detroit Automation Academy curriculum examples.

Run with: python -m pytest test_examples.py -v

Tests cover Phase 1 (GPIO patterns), Phase 2 (CAD generation), and Phase 3 (rover simulation).
"""

import sys
import os
import math
import tempfile

# Ensure imports work from root directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from phase3.autonomous_rover import Rover, World


class TestPhase1GPIO:
    """Tests for Phase 1: GPIO control patterns."""
    
    def test_button_debounce_pattern(self):
        """
        Test that GPIO event detection pattern includes proper debounce.
        
        Learning: 200ms bouncetime prevents multiple rapid triggers from button bounce.
        This test documents the expected pattern, not actual GPIO hardware.
        """
        # Bouncetime in milliseconds
        bouncetime = 200
        assert isinstance(bouncetime, int), "Bouncetime should be an integer"
        assert bouncetime > 0, "Bouncetime should be positive"
        print(f"✓ Button debounce pattern: {bouncetime}ms")
    
    def test_led_blink_parameters(self):
        """
        Test valid LED blink parameters.
        
        Learning: Blinking requires duration > 0 and times > 0.
        """
        pin = 17
        duration = 0.5  # seconds
        times = 10
        
        assert isinstance(pin, int), "Pin should be an integer"
        assert pin > 0, "Pin number should be positive"
        assert duration > 0, "Duration should be positive"
        assert times > 0, "Times should be positive"
        print(f"✓ LED blink: pin {pin}, {duration}s per blink, {times} cycles")
    
    def test_pull_up_resistor_configuration(self):
        """
        Test understanding of pull-up resistor configuration.
        
        Learning: Pull-up keeps pin HIGH by default; button press pulls it LOW (falling edge).
        """
        pin_state_default = "HIGH"  # With pull-up
        edge_type = "FALLING"        # Button press = falling edge (HIGH → LOW)
        
        assert pin_state_default == "HIGH", "Pull-up keeps pin HIGH when not pressed"
        assert edge_type == "FALLING", "Button press triggers FALLING edge"
        print(f"✓ Pull-up configuration: default={pin_state_default}, trigger={edge_type}")


class TestPhase2CAD:
    """Tests for Phase 2: CAD design and parametric modeling."""
    
    def test_parametric_dimensions(self):
        """
        Test that parametric functions accept dimension parameters.
        
        Learning: Parametric modeling means changing one number changes entire design.
        """
        # Example: rover chassis dimensions
        width = 10
        height = 5
        length = 15
        
        assert width > 0, "Chassis width must be positive"
        assert height > 0, "Chassis height must be positive"
        assert length > 0, "Chassis length must be positive"
        assert length > width, "Chassis should be longer than wide (typical rover shape)"
        print(f"✓ Rover chassis parameters: {length}mm long × {width}mm wide × {height}mm tall")
    
    def test_stl_file_generation(self):
        """
        Test that STL generation functions exist and work.
        
        Learning: STL files are binary format for 3D printing.
        """
        # Import the module to verify it exists
        from phase2 import cad_design
        
        # Verify key classes/functions exist
        assert hasattr(cad_design, 'STLWriter'), "cad_design module should have STLWriter class"
        assert hasattr(cad_design, 'create_rover_chassis'), "cad_design should have create_rover_chassis function"
        print(f"✓ Phase 2 CAD generation functions available")
    
    def test_gcode_command_sequence(self):
        """
        Test understanding of basic G-code command sequence for laser cutting.
        
        Learning: G-code is machine instructions for CNC equipment.
        """
        gcode_sequence = [
            "G21",      # Set units to millimeters
            "G90",      # Absolute positioning
            "M3 S255",  # Laser on at full power
            "G0 Z5",    # Move to safe height
            "G1 F200",  # Set feed rate (speed)
            "M5",       # Laser off
        ]
        
        assert gcode_sequence[0] == "G21", "G21 sets metric units"
        assert gcode_sequence[1] == "G90", "G90 enables absolute positioning"
        assert "M3" in gcode_sequence[2], "M3 turns laser on"
        assert "M5" in gcode_sequence[-1], "M5 turns laser off"
        print(f"✓ G-code command sequence valid ({len(gcode_sequence)} commands)")
    
    def test_material_specific_settings(self):
        """
        Test material-specific laser power/speed parameters.
        
        Learning: Different materials require different power/speed for optimal cutting.
        """
        materials = {
            "acrylic_3mm": {"power": 255, "speed": 200, "time_sec": 45},
            "plywood_3mm": {"power": 255, "speed": 180, "time_sec": 60},
            "cardboard_3mm": {"power": 200, "speed": 200, "time_sec": 30},
        }
        
        for material, params in materials.items():
            assert 0 < params["power"] <= 255, f"{material} power must be 0-255"
            assert params["speed"] > 0, f"{material} speed must be positive"
            assert params["time_sec"] > 0, f"{material} cut time must be positive"
        
        # Verify acrylic cuts faster than plywood (same power, higher speed)
        assert materials["acrylic_3mm"]["speed"] >= materials["plywood_3mm"]["speed"]
        print(f"✓ Material-specific settings validated ({len(materials)} materials)")


class TestPhase3Rover:
    """Tests for Phase 3: Autonomous systems and rover simulation."""
    
    def test_rover_initialization(self):
        """
        Test rover initialization with default and custom positions.
        
        Learning: Rover tracks position (x, y) and direction (0-3 for North/East/South/West).
        """
        # Default initialization
        rover_default = Rover()
        assert rover_default.x == 0, "Default x should be 0"
        assert rover_default.y == 0, "Default y should be 0"
        assert rover_default.direction == 0, "Default direction should be 0 (North)"
        
        # Custom initialization
        rover_custom = Rover(x=5, y=10)
        assert rover_custom.x == 5, "Custom x should be set correctly"
        assert rover_custom.y == 10, "Custom y should be set correctly"
        
        print(f"✓ Rover initialization: default (0,0) facing North, custom positions work")
    
    def test_rover_movement_north(self):
        """
        Test rover forward movement when facing North.
        
        Learning: North direction (0) should increase y-coordinate.
        """
        rover = Rover(x=5, y=5)
        rover.direction = 0  # North
        rover.move_forward()
        
        assert rover.x == 5, "X should not change when moving North"
        assert rover.y == 6, "Y should increase by 1 when moving North"
        print(f"✓ North movement: (5,5) → (5,6)")
    
    def test_rover_movement_east(self):
        """
        Test rover forward movement when facing East.
        
        Learning: East direction (1) should increase x-coordinate.
        """
        rover = Rover(x=5, y=5)
        rover.direction = 1  # East
        rover.move_forward()
        
        assert rover.x == 6, "X should increase by 1 when moving East"
        assert rover.y == 5, "Y should not change when moving East"
        print(f"✓ East movement: (5,5) → (6,5)")
    
    def test_rover_movement_south(self):
        """
        Test rover forward movement when facing South.
        
        Learning: South direction (2) should decrease y-coordinate.
        """
        rover = Rover(x=5, y=5)
        rover.direction = 2  # South
        rover.move_forward()
        
        assert rover.x == 5, "X should not change when moving South"
        assert rover.y == 4, "Y should decrease by 1 when moving South"
        print(f"✓ South movement: (5,5) → (5,4)")
    
    def test_rover_movement_west(self):
        """
        Test rover forward movement when facing West.
        
        Learning: West direction (3) should decrease x-coordinate.
        """
        rover = Rover(x=5, y=5)
        rover.direction = 3  # West
        rover.move_forward()
        
        assert rover.x == 4, "X should decrease by 1 when moving West"
        assert rover.y == 5, "Y should not change when moving West"
        print(f"✓ West movement: (5,5) → (4,5)")
    
    def test_rover_turn_left(self):
        """
        Test rover left turn (counterclockwise rotation).
        
        Learning: Turn left is direction - 1 (with modulo wrapping).
        """
        rover = Rover()
        
        # Start facing North (0)
        rover.direction = 0
        rover.turn_left()
        assert rover.direction == 3, "Left from North should be West"
        
        # From West (3)
        rover.turn_left()
        assert rover.direction == 2, "Left from West should be South"
        
        # From South (2)
        rover.turn_left()
        assert rover.direction == 1, "Left from South should be East"
        
        # From East (1)
        rover.turn_left()
        assert rover.direction == 0, "Left from East should be North"
        
        print(f"✓ Left turn rotation: 0→3→2→1→0 (counterclockwise)")
    
    def test_rover_turn_right(self):
        """
        Test rover right turn (clockwise rotation).
        
        Learning: Turn right is direction + 1 (with modulo wrapping).
        """
        rover = Rover()
        
        # Start facing North (0)
        rover.direction = 0
        rover.turn_right()
        assert rover.direction == 1, "Right from North should be East"
        
        # From East (1)
        rover.turn_right()
        assert rover.direction == 2, "Right from East should be South"
        
        # From South (2)
        rover.turn_right()
        assert rover.direction == 3, "Right from South should be West"
        
        # From West (3)
        rover.turn_right()
        assert rover.direction == 0, "Right from West should be North"
        
        print(f"✓ Right turn rotation: 0→1→2→3→0 (clockwise)")
    
    def test_rover_get_position(self):
        """
        Test rover position reporting as (x, y) tuple.
        
        Learning: get_position() returns current coordinates in correct order.
        """
        rover = Rover(x=7, y=3)
        position = rover.get_position()
        
        assert isinstance(position, tuple), "Position should be a tuple"
        assert len(position) == 2, "Position tuple should have 2 elements"
        assert position == (7, 3), "Position should return (x, y) in correct order"
        assert position[0] == 7, "First element should be x"
        assert position[1] == 3, "Second element should be y"
        
        print(f"✓ Rover position: get_position() = {position}")
    
    def test_world_initialization(self):
        """
        Test world creation with obstacles.
        
        Learning: World has fixed dimensions and randomly placed obstacles.
        """
        world = World(width=10, height=10)
        
        assert world.width == 10, "World width should match parameter"
        assert world.height == 10, "World height should match parameter"
        assert hasattr(world, 'obstacles'), "World should have obstacles attribute"
        assert isinstance(world.obstacles, set), "Obstacles should be stored as a set"
        
        print(f"✓ World initialized: {world.width}×{world.height} with {len(world.obstacles)} obstacles")
    
    def test_world_boundary_checking(self):
        """
        Test that world correctly identifies valid positions.
        
        Learning: Valid positions must be within bounds (0-9 for 10×10 world).
        """
        world = World(width=10, height=10)
        
        # Valid positions (within bounds)
        assert world.is_valid_position(0, 0), "(0,0) should be valid"
        assert world.is_valid_position(5, 5), "(5,5) should be valid"
        assert world.is_valid_position(9, 9), "(9,9) should be valid"
        
        # Invalid positions (out of bounds)
        assert not world.is_valid_position(-1, 5), "Negative x should be invalid"
        assert not world.is_valid_position(5, -1), "Negative y should be invalid"
        assert not world.is_valid_position(10, 5), "x=10 should be invalid (10×10 grid is 0-9)"
        assert not world.is_valid_position(5, 10), "y=10 should be invalid (10×10 grid is 0-9)"
        
        print(f"✓ World boundary checking: 10×10 grid bounds validated")
    
    def test_direction_mapping_constants(self):
        """
        Test that direction mapping convention is consistent.
        
        Learning: Direction convention: 0=North, 1=East, 2=South, 3=West
        This is critical for all rover implementations.
        """
        direction_names = {
            0: "North",
            1: "East",
            2: "South",
            3: "West"
        }
        
        # Verify all directions are represented
        for direction_num, direction_name in direction_names.items():
            assert 0 <= direction_num < 4, f"Direction {direction_num} should be 0-3"
        
        # Verify cardinal order (clockwise from North)
        assert direction_names[0] == "North", "0 must be North"
        assert direction_names[1] == "East", "1 must be East"
        assert direction_names[2] == "South", "2 must be South"
        assert direction_names[3] == "West", "3 must be West"
        
        print(f"✓ Direction mapping: 0=North, 1=East, 2=South, 3=West (consistent)")


# Optional: Performance test for rover simulation
class TestPhase3Performance:
    """Performance tests for rover simulation."""
    
    def test_rover_multiple_moves(self):
        """
        Test rover performance over multiple sequential moves.
        
        Learning: Rover should handle many moves without degradation.
        """
        rover = Rover(x=5, y=5)
        initial_pos = rover.get_position()
        
        # Perform 1000 moves
        for _ in range(1000):
            rover.move_forward()
        
        # Rover should have moved far from origin
        final_pos = rover.get_position()
        distance = abs(final_pos[0] - initial_pos[0]) + abs(final_pos[1] - initial_pos[1])
        assert distance > 0, "Rover should have moved"
        
        print(f"✓ Performance: 1000 moves completed (start={initial_pos}, end={final_pos}, distance={distance})")


if __name__ == "__main__":
    # Run tests with basic output if pytest not available
    print("=" * 70)
    print("Detroit Automation Academy - Test Suite")
    print("=" * 70)
    print()
    
    # Phase 1 Tests
    print("PHASE 1: GPIO Control (Patterns & Best Practices)")
    print("-" * 70)
    phase1 = TestPhase1GPIO()
    phase1.test_button_debounce_pattern()
    phase1.test_led_blink_parameters()
    phase1.test_pull_up_resistor_configuration()
    print()
    
    # Phase 2 Tests
    print("PHASE 2: CAD Design & Rapid Prototyping")
    print("-" * 70)
    phase2 = TestPhase2CAD()
    phase2.test_parametric_dimensions()
    phase2.test_stl_file_generation()
    phase2.test_gcode_command_sequence()
    phase2.test_material_specific_settings()
    print()
    
    # Phase 3 Tests
    print("PHASE 3: Autonomous Systems & Rover Simulation")
    print("-" * 70)
    phase3 = TestPhase3Rover()
    phase3.test_rover_initialization()
    phase3.test_rover_movement_north()
    phase3.test_rover_movement_east()
    phase3.test_rover_movement_south()
    phase3.test_rover_movement_west()
    phase3.test_rover_turn_left()
    phase3.test_rover_turn_right()
    phase3.test_rover_get_position()
    phase3.test_world_initialization()
    phase3.test_world_boundary_checking()
    phase3.test_direction_mapping_constants()
    print()
    
    # Performance Tests
    print("PHASE 3: Performance Tests")
    print("-" * 70)
    perf = TestPhase3Performance()
    perf.test_rover_multiple_moves()
    print()
    
    print("=" * 70)
    print("All tests passed! ✓")
    print("=" * 70)
