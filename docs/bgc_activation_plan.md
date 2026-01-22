# Boys & Girls Club Grand Opening: Activation Content Plan

**Dates:** February 3rd & 4th, 2026
**Location:** Boys & Girls Club (Grand Opening Event)
**Objective:** Showcase student "Physical Computing" skills through interactive, hands-on stations.

## Activation Zones
To manage flow and showcase the full curriculum, the space will be divided into three stations.

### Zone 1: The "Design Lab" (Software & Git)
*Best for: Interactive coding, understanding the "Digital Thread".*
*   **Hardware:** Laptops/Tablets with Terminal, Git & Python installed.
*   **Activity:** **"Git the Gear"**
    *   Guests "retrieve" the design by cloning the repo (or pulling latest changes).
    *   Run the script to generate the custom token file: `python3 phase2/cad_design.py`
    *   **Code Reference:** `phase2/cad_design.py` (Generates `gear_token.stl`).
*   **Student Role:** Guide guests through the terminal commands and explain how Python code defines physical geometry.

### Zone 2: The "Body" (Rapid Prototyping)
*Best for: Visual spectacle, Souvenirs.*
*   **Hardware:** Bambu Lab A1 (Bed Slinger), X1 Carbon (CoreXY), Epilog Fusion Maker (Laser).
*   **Activity:** **"Fabrication Station"**
    *   **Live Demo:** Printing B&G Club commemorative tokens (approx. 15 min print time).
    *   **Comparison:** Showcasing the speed difference between the A1 and X1 Carbon.
    *   **Code Reference:** `phase2/cad_design.py` (The file generated in Zone 1 is sliced here).
    *   **Design Concepts:** Token Design Concepts
*   **Student Role:** Hand out finished tokens and explain how 3D slicing works.

### Zone 3: The "Future" (Autonomous Systems)
*Best for: Extended engagement, "Wow" factor.*
*   **Hardware:** Rover Kit (or Simulation Screen).
*   **Activity:** **"The Maze Run"**
    *   A taped-out grid on the floor.
    *   Rover attempts to navigate autonomously using the obstacle avoidance logic.
    *   **Interactive Element:** Guests place cardboard obstacles in the path to see if the rover detects them.
    *   **Code Reference:** `phase3/autonomous_rover.py`
*   **Student Role:** Reset the rover and explain the "Sensor Fusion" concept.

---

## Schedule & Content Strategy

### Monday, Feb 3rd (60-Minute Slots)
*Context: High traffic, guests walking through. Focus on visual/fast interactions.*

*   **4:00 PM – 5:00 PM:** **Visual Mode.**
    *   3D Printers running continuously.
    *   Rovers running in "Demo Mode" (looping path).
*   **6:00 PM – 7:00 PM:** **Interactive Mode.**
    *   Students invite guests to generate their own token file at Zone 1.

### Tuesday, Feb 4th (90-Minute Slots)
*Context: Longer duration, likely school groups or deeper community engagement.*

*   **9:00 AM & 11:00 AM:** **Mini-Workshops.**
    *   **Zone 1:** 10-minute "Code to CAD" session (Generate STL).
    *   **Zone 3:** "Robot Race" – Students explain the logic, then run the rover.
*   **4:30 PM:** **Community Challenge.**
    *   **"Human vs. Machine":** A guest tries to drive a remote-control rover through the maze faster than the autonomous rover can navigate it.

## Resource & Staffing Distribution

### Staffing Rotation
*   **Total Students Needed:** 4-6 per shift.
*   **Zone 1 (Design Lab):** 1 Student (Guiding terminal commands).
*   **Zone 2 (The Body):** 2 Students (1 running printers, 1 managing token distribution).
*   **Zone 3 (The Future):** 1-2 Students (Resetting rover, managing crowd control).
*   **Floater:** 1 Student (Photos, breaks, guiding guests).

### Swag Distribution Strategy (The "Token Economy")
*   **Inventory:** 50 Pre-printed Tokens + Live prints (~4/hour).
*   **Constraint:** ~100 Guests expected.
*   **Distribution Logic:** To prevent running out early, tokens are reserved for guests who engage deeply.
    1.  **"The Passport":** Guests receive a card upon entry.
    2.  **Engagement:** They must complete a micro-activity at Zone 1 or Zone 3 to get a stamp.
    3.  **Reward:** A stamped passport can be redeemed at Zone 2 for a fresh token.

## Logistics Checklist
- [ ] **Power:** Extension cords for 3D printers and monitors.
- [ ] **WiFi:** Verify connection for Laptops (Git cloning) and Zone 3 Rovers.
- [ ] **Swag:** Pre-print 50 tokens on the Bambu Lab printers before the event.
- [ ] **Design:** Verify `phase2/cad_design.py` generates `gear_token.stl` correctly on lab laptops.
- [ ] **Safety:** Tape down all cables; install safety shields on Epilog Fusion Maker.