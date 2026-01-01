import struct

class STLWriter:
    """Simple STL writer for 3D printing."""
    def __init__(self, filename):
        self.filename = filename
        self.triangles = []

    def add_triangle(self, v1, v2, v3):
        # Normal calculation is simplified to (0,0,0) for this example
        # Slicers typically recalculate normals automatically
        self.triangles.append(((0,0,0), v1, v2, v3))

    def add_cuboid(self, x, y, z, w, h, d):
        """Add a rectangular box (cuboid) to the model.
        
        Args:
            x, y, z: Origin coordinates
            w, h, d: Width, Height, Depth
        """
        # Vertices
        v = [
            (x, y, z), (x+w, y, z), (x+w, y+h, z), (x, y+h, z),         # Front face
            (x, y, z+d), (x+w, y, z+d), (x+w, y+h, z+d), (x, y+h, z+d)  # Back face
        ]
        
        # Define the 12 triangles that make up the cube
        # Front
        self.add_triangle(v[0], v[1], v[2])
        self.add_triangle(v[0], v[2], v[3])
        # Back
        self.add_triangle(v[5], v[4], v[7])
        self.add_triangle(v[5], v[7], v[6])
        # Left
        self.add_triangle(v[4], v[0], v[3])
        self.add_triangle(v[4], v[3], v[7])
        # Right
        self.add_triangle(v[1], v[5], v[6])
        self.add_triangle(v[1], v[6], v[2])
        # Top
        self.add_triangle(v[3], v[2], v[6])
        self.add_triangle(v[3], v[6], v[7])
        # Bottom
        self.add_triangle(v[4], v[5], v[1])
        self.add_triangle(v[4], v[1], v[0])

    def write(self):
        """Write the geometry to the STL file."""
        with open(self.filename, 'wb') as f:
            f.write(b'\x00' * 80) # Header
            f.write(struct.pack('<I', len(self.triangles)))
            for normal, v1, v2, v3 in self.triangles:
                f.write(struct.pack('<3f', *normal))
                f.write(struct.pack('<3f', *v1))
                f.write(struct.pack('<3f', *v2))
                f.write(struct.pack('<3f', *v3))
                f.write(b'\x00\x00') # Attribute byte count

def create_modular_chassis():
    """Generates a modern modular rover chassis."""
    print("Generating modular rover chassis...")
    stl = STLWriter("rover_chassis.stl")
    
    # 1. Main Platform Base
    length = 120
    width = 80
    thickness = 4
    stl.add_cuboid(0, 0, 0, length, width, thickness)
    
    # 2. Reinforced Side Rails
    rail_width = 6
    rail_height = 12
    stl.add_cuboid(0, 0, thickness, length, rail_width, rail_height) # Left Rail
    stl.add_cuboid(0, width-rail_width, thickness, length, rail_width, rail_height) # Right Rail
    
    # 3. Modular Mounting Grid (3x3)
    # Adds raised blocks for mounting sensors/controllers
    margin = 20
    spacing_x = (length - 2*margin) / 2
    spacing_y = (width - 2*margin) / 2
    
    for i in range(3):
        for j in range(3):
            mx = margin + i * spacing_x
            my = margin + j * spacing_y
            stl.add_cuboid(mx-4, my-4, thickness, 8, 8, 3)

    # 4. External Wheel Mounts
    mount_w = 15
    mount_ext = 10
    # Front & Back, Left & Right
    stl.add_cuboid(15, -mount_ext, 0, mount_w, mount_ext, 8) # FL
    stl.add_cuboid(15, width, 0, mount_w, mount_ext, 8)      # FR
    stl.add_cuboid(length-30, -mount_ext, 0, mount_w, mount_ext, 8) # BL
    stl.add_cuboid(length-30, width, 0, mount_w, mount_ext, 8)      # BR

    stl.write()
    print(f"Success! Created rover_chassis.stl ({length}x{width}mm)")

if __name__ == "__main__":
    create_modular_chassis()