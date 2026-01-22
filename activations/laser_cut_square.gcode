; Detroit Automation Academy - Laser Cutting
G21 ; Set units to millimeters
G90 ; Absolute positioning
M3 S255 ; Laser on at full power
G0 Z5 ; Move to safe height
G0 X0 Y0 ; Move to start
G1 Z-1 F100 ; Lower to cutting depth
G1 X15 Y0 F200 ; Cut to right
G1 X15 Y15 ; Cut up
G1 X0 Y15 ; Cut left
G1 X0 Y0 ; Cut down
G0 Z5 ; Raise to safe height
M5 ; Laser off
G0 X0 Y0 ; Return to origin
M30 ; End program
