# Challenge Based Learning

Welcome to the Challenge Based Learning module of the Detroit Automation Academy.
Here you will find scenarios where things have gone wrong, and it is your job to fix them.

## Challenge 1: The Confused Rover
**File:** `challenges/challenge_1_rover_debug.py`

**Scenario:**
Our prototype rover has been deployed for testing, but the telemetry data is making no sense.
The engineering team needs you to look at the code and fix the following critical bugs:

1.  **Directional Error:** The rover seems to get confused about North vs South.
2.  **Power Leak:** The battery is draining significantly faster than the spec sheet says (should be 1% per move).
3.  **Boundary Safety:** The rover is allowed to move into negative coordinates, which represents a restricted zone.

**Goal:**
Debug the script so the rover moves correctly, manages power efficiently, and stays within safe bounds (coordinates >= 0).
