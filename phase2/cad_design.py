#!/usr/bin/env python3
"""
Phase 2: CAD Design & Rapid Prototyping
Example: Parametric 3D Model Generator

This script demonstrates generating parametric 3D models using basic geometry.
It creates STL files that can be used for 3D printing.
"""

import math
import struct

class STLWriter:
    """
    Simple STL file writer for generating 3D printable models.
    STL (STereoLithography) is a file format for 3D printing.
    """

    def __init__(self, filename):
        self.filename = filename
        self.triangles = []

    def add_triangle(self, v1, v2, v3, normal=None):
        """
        Add a triangle to the model.

        Args:
            v1, v2, v3: Vertices as (x, y, z) tuples
            normal: Normal vector as (x, y, z) tuple (auto-calculated if None)
        """
        if normal is None:
            # Calculate normal vector
            u = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
            v = (v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2])
            normal = (
                u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0]
            )
            # Normalize
            length = math.sqrt(sum(x**2 for x in normal))
            if length > 0:
                normal = tuple(x / length for x in normal)

        self.triangles.append((normal, v1, v2, v3))

    def write(self):
        """Write the STL file."""
        with open(self.filename, 'wb') as f:
            # STL header (80 bytes)
            header = b'Detroit Automation Academy - Parametric Model' + b'\x00' * (80 - len(b'Detroit Automation Academy - Parametric Model'))
            f.write(header)

            # Number of triangles (4 bytes, little endian)
            f.write(struct.pack('<I', len(self.triangles)))

            # Write each triangle
            for normal, v1, v2, v3 in self.triangles:
                # Normal vector (3 floats)
                f.write(struct.pack('<fff', *normal))
                # Vertices (3 floats each)
                f.write(struct.pack('<fff', *v1))
                f.write(struct.pack('<fff', *v2))
                f.write(struct.pack('<fff', *v3))
                # Attribute byte count (2 bytes)
                f.write(struct.pack('<H', 0))

def add_cuboid(stl, x, y, z, dx, dy, dz):
    """
    Helper to add a cuboid (box) to an STL writer.
    
    Args:
        stl (STLWriter): The STL writer instance
        x, y, z (float): Origin coordinates (bottom-front-left)
        dx, dy, dz (float): Dimensions in x, y, and z
    """
    vertices = [
        (x, y, z),              # 0
        (x + dx, y, z),         # 1
        (x + dx, y + dy, z),    # 2
        (x, y + dy, z),         # 3
        (x, y, z + dz),         # 4
        (x + dx, y, z + dz),    # 5
        (x + dx, y + dy, z + dz), # 6
        (x, y + dy, z + dz),    # 7
    ]
    faces = [
        (0, 1, 2), (0, 2, 3), (4, 5, 6), (4, 6, 7), # Bottom, Top
        (0, 1, 5), (0, 5, 4), (3, 2, 6), (3, 6, 7), # Front, Back
        (0, 3, 7), (0, 7, 4), (1, 2, 6), (1, 6, 5), # Left, Right
    ]
    for face in faces:
        v1, v2, v3 = [vertices[i] for i in face]
        stl.add_triangle(v1, v2, v3)

def create_rover_chassis(width=10, height=5, length=15):
    """
    Create a simple rover chassis model.

    Args:
        width (float): Width of the chassis
        height (float): Height of the chassis
        length (float): Length of the chassis
    """
    stl = STLWriter('rover_chassis.stl')

    # Define vertices for a simple box chassis
    vertices = [
        (0, 0, 0),      # 0: bottom front left
        (length, 0, 0), # 1: bottom front right
        (length, width, 0), # 2: bottom back right
        (0, width, 0),  # 3: bottom back left
        (0, 0, height), # 4: top front left
        (length, 0, height), # 5: top front right
        (length, width, height), # 6: top back right
        (0, width, height), # 7: top back left
    ]

    # Define faces (triangles)
    faces = [
        # Bottom face
        (0, 1, 2), (0, 2, 3),
        # Top face
        (4, 5, 6), (4, 6, 7),
        # Front face
        (0, 1, 5), (0, 5, 4),
        # Back face
        (3, 2, 6), (3, 6, 7),
        # Left face
        (0, 3, 7), (0, 7, 4),
        # Right face
        (1, 2, 6), (1, 6, 5),
    ]

    for face in faces:
        v1, v2, v3 = [vertices[i] for i in face]
        stl.add_triangle(v1, v2, v3)

    stl.write()
    print(f"Created rover chassis model: {stl.filename}")

def create_sensor_mount(radius=2, height=3):
    """
    Create a cylindrical sensor mount.

    Args:
        radius (float): Radius of the cylinder
        height (float): Height of the cylinder
    """
    stl = STLWriter('sensor_mount.stl')

    # Create a simple cylinder approximation
    segments = 16
    angle_step = 2 * math.pi / segments

    # Bottom vertices
    bottom_center = (0, 0, 0)
    bottom_vertices = []
    for i in range(segments):
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        bottom_vertices.append((x, y, 0))

    # Top vertices
    top_center = (0, 0, height)
    top_vertices = []
    for i in range(segments):
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        top_vertices.append((x, y, height))

    # Bottom face
    for i in range(segments):
        v1 = bottom_center
        v2 = bottom_vertices[i]
        v3 = bottom_vertices[(i + 1) % segments]
        stl.add_triangle(v1, v2, v3)

    # Top face
    for i in range(segments):
        v1 = top_center
        v2 = top_vertices[i]
        v3 = top_vertices[(i + 1) % segments]
        stl.add_triangle(v1, v3, v2)  # Reverse order for correct normal

    # Side faces
    for i in range(segments):
        # Two triangles per side segment
        v1 = bottom_vertices[i]
        v2 = bottom_vertices[(i + 1) % segments]
        v3 = top_vertices[i]
        v4 = top_vertices[(i + 1) % segments]

        stl.add_triangle(v1, v2, v3)
        stl.add_triangle(v2, v4, v3)

    stl.write()
    print(f"Created sensor mount model: {stl.filename}")

def create_gear_token(diameter=40, thickness=5, teeth=6):
    """
    Create the 'Future Gear' token for the B&G Club event.
    
    Args:
        diameter (float): Outer diameter of the gear
        thickness (float): Thickness of the token
        teeth (int): Number of gear teeth
    """
    stl = STLWriter('gear_token.stl')
    radius = diameter / 2
    segments = 72  # High resolution for smooth curves
    
    # Generate vertices for the gear profile (sine wave approximation for teeth)
    bottom_vertices = []
    top_vertices = []
    
    for i in range(segments):
        angle = i * 2 * math.pi / segments
        # Modulate radius to create teeth: Base radius + sine wave offset
        # Using 0.85 factor for inner radius of teeth
        r = radius * (0.85 + 0.15 * math.sin(teeth * angle))
        
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        
        bottom_vertices.append((x, y, 0))
        top_vertices.append((x, y, thickness))

    # Create faces
    center_bottom = (0, 0, 0)
    center_top = (0, 0, thickness)

    for i in range(segments):
        next_i = (i + 1) % segments
        
        # Bottom face (fan)
        stl.add_triangle(center_bottom, bottom_vertices[next_i], bottom_vertices[i])
        
        # Top face (fan)
        stl.add_triangle(center_top, top_vertices[i], top_vertices[next_i])
        
        # Side walls (2 triangles per segment)
        stl.add_triangle(bottom_vertices[i], bottom_vertices[next_i], top_vertices[i])
        stl.add_triangle(bottom_vertices[next_i], top_vertices[next_i], top_vertices[i])

    stl.write()
    print(f"Created gear token model: {stl.filename}")

def create_skyline_keychain(filename='skyline_keychain.stl'):
    """
    Create the 'Detroit Skyline' Keychain (Concept 3).
    Features a base tag with low-poly building blocks.
    """
    stl = STLWriter(filename)
    
    # Base Tag (50mm x 30mm x 2mm)
    add_cuboid(stl, 0, 0, 0, 50, 30, 2)
    
    # Skyline Buildings (Low-poly relief)
    # Building 1 (Renaissance Center style central tower)
    add_cuboid(stl, 20, 5, 2, 10, 20, 15)
    # Building 2 (Left tower)
    add_cuboid(stl, 5, 5, 2, 10, 15, 8)
    # Building 3 (Right tower)
    add_cuboid(stl, 35, 5, 2, 10, 12, 6)
    
    # Keyring Loop (Approximated with 3 blocks forming a C shape)
    add_cuboid(stl, -5, 10, 0, 5, 2, 2)   # Bottom strut
    add_cuboid(stl, -5, 20, 0, 5, 2, 2)   # Top strut
    add_cuboid(stl, -7, 10, 0, 2, 12, 2)  # Connector
    
    stl.write()
    print(f"Created skyline keychain model: {stl.filename}")

def create_robot_head(filename='robot_head.stl'):
    """
    Create the 'Robot Head' Token (Concept 4).
    A simple 2D extruded icon.
    """
    stl = STLWriter(filename)
    
    # Face Base (40mm x 40mm)
    add_cuboid(stl, 0, 0, 0, 40, 40, 3)
    
    # Eyes (Raised blocks)
    add_cuboid(stl, 8, 22, 3, 8, 8, 2)
    add_cuboid(stl, 24, 22, 3, 8, 8, 2)
    
    # Mouth (Wide block)
    add_cuboid(stl, 10, 8, 3, 20, 6, 2)
    
    # Antenna
    add_cuboid(stl, 18, 40, 0, 4, 6, 3)
    
    stl.write()
    print(f"Created robot head model: {stl.filename}")

def generate_gcode_for_laser_cutting(shape="square", size=10):
    """
    Generate G-code for laser cutting a simple shape.

    Args:
        shape (str): Shape to cut ("square", "circle", "triangle")
        size (float): Size of the shape
    """
    filename = f"laser_cut_{shape}.gcode"

    with open(filename, 'w') as f:
        # G-code header
        f.write("; Detroit Automation Academy - Laser Cutting\n")
        f.write("G21 ; Set units to millimeters\n")
        f.write("G90 ; Absolute positioning\n")
        f.write("M3 S255 ; Laser on at full power\n")
        f.write("G0 Z5 ; Move to safe height\n")

        if shape == "square":
            # Square cutting path
            f.write(f"G0 X0 Y0 ; Move to start\n")
            f.write("G1 Z-1 F100 ; Lower to cutting depth\n")
            f.write(f"G1 X{size} Y0 F200 ; Cut to right\n")
            f.write(f"G1 X{size} Y{size} ; Cut up\n")
            f.write(f"G1 X0 Y{size} ; Cut left\n")
            f.write("G1 X0 Y0 ; Cut down\n")

        elif shape == "circle":
            # Circular cutting path (approximated)
            f.write("G0 X0 Y0 ; Move to center\n")
            f.write("G1 Z-1 F100 ; Lower to cutting depth\n")
            f.write("G2 X0 Y0 I0 J5 F200 ; Cut circle\n")

        elif shape == "triangle":
            # Triangle cutting path
            f.write("G0 X0 Y0 ; Move to start\n")
            f.write("G1 Z-1 F100 ; Lower to cutting depth\n")
            f.write(f"G1 X{size} Y0 F200 ; Cut to right\n")
            f.write(f"G1 X{size/2} Y{size * 0.866} ; Cut to top\n")
            f.write("G1 X0 Y0 ; Cut back to start\n")

        # G-code footer
        f.write("G0 Z5 ; Raise to safe height\n")
        f.write("M5 ; Laser off\n")
        f.write("G0 X0 Y0 ; Return to origin\n")
        f.write("M30 ; End program\n")

    print(f"Generated G-code for laser cutting: {filename}")

if __name__ == "__main__":
    print("Detroit Automation Academy - CAD Design Examples")
    print("=" * 50)

    # Generate 3D models
    print("\nGenerating 3D models...")
    create_rover_chassis(width=12, height=6, length=18)
    create_sensor_mount(radius=3, height=4)
    create_gear_token(diameter=40, thickness=5, teeth=6)
    create_skyline_keychain()
    create_robot_head()

    # Generate laser cutting G-code
    print("\nGenerating laser cutting files...")
    generate_gcode_for_laser_cutting("square", 15)
    generate_gcode_for_laser_cutting("circle", 10)
    generate_gcode_for_laser_cutting("triangle", 12)

    print("\nCAD design examples complete!")
    print("Files generated:")
    print("- rover_chassis.stl (3D printable rover chassis)")
    print("- sensor_mount.stl (3D printable sensor mount)")
    print("- gear_token.stl (B&G Club Event Token)")
    print("- skyline_keychain.stl (Concept 3)")
    print("- robot_head.stl (Concept 4)")
    print("- laser_cut_*.gcode (laser cutting files)")