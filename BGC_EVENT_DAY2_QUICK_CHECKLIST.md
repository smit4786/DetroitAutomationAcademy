# ✅ BGC EVENT DAY 2 - QUICK REFERENCE CHECKLIST
**February 4, 2026 | 10:00 AM - 1:00 PM**

---

## 📋 JUSTIN SMITH - EVENT COORDINATOR CHECKLIST

### Before Event (Arrive 8:45 AM)
- [ ] Walk all three zones (equipment status)
- [ ] Verify emergency contact list posted at each zone
- [ ] Check registration table setup (sign-in sheets, forms, pens)
- [ ] Meet with Zone Leads (5-min sync per zone)
- [ ] Brief media contacts (if present)

### 9:45 AM - All-Hands Staff Briefing (15 min)
- [ ] Gather all 18 staff
- [ ] Quick review: event flow, talking points (2-3 min per zone)
- [ ] Emergency procedures reminder
- [ ] Confirm everyone has emergency contact list
- [ ] **GO!** - Event starts at 10:00 AM

### During Event - Hourly Checkpoints

**10:30 AM Checkpoint**
- [ ] Walk all zones - equipment functional?
- [ ] Any immediate issues? Report to Zone Leads

**11:00 AM Checkpoint**
- [ ] Check sign-in sheet count (running total)
- [ ] Any capacity problems?
- [ ] Report to Nicole

**11:30 AM Checkpoint**
- [ ] Zone 2: Acrylic blank supply OK?
- [ ] Zone 3: Rover battery levels?
- [ ] Token distribution tracking

**12:00 PM Checkpoint** (MEDIA HOUR)
- [ ] Capture high-res photos at all zones
- [ ] Are journalists present? Schedule interviews
- [ ] Brief Justin Smith on media contacts

**12:30 PM Checkpoint**
- [ ] Make announcement: "30 minutes remaining!"
- [ ] Encourage interest form completion
- [ ] Final surge push

### Post-Event (1:00 PM - 2:00 PM)
- [ ] Coordinate teardown
- [ ] Collect all sign-in sheets
- [ ] Count interest forms (with Nicole)
- [ ] Count tokens distributed
- [ ] Staff debrief (5-10 min)
- [ ] Compile preliminary numbers
- [ ] **DELIVER:** Report to leadership by 6:00 PM

### Key Phone Numbers
- Justin Smith: (313) 306-3767
- Facility Manager: [Insert]
- Emergency: 911

---

## 📋 NICOLE YUNGERS - OPERATIONS CHECKLIST

### Before Event (Arrive 8:45 AM)
- [ ] Registration table: sign-in sheets, forms, pens, clipboards, name tags
- [ ] Verify all materials printed and ready:
  - [ ] 125 interest forms
  - [ ] 2 sign-in sheets
  - [ ] 125 brochures
  - [ ] 50 business cards (Justin's)
  - [ ] 30 cheat sheets per zone (Zone 1, 2, 3)
- [ ] Signage in place: banner, directional signs, QR posters
- [ ] All zones stocked with materials

### During Event (10:00 AM - 1:00 PM)

**10:30 AM Check**
- [ ] All supplies at full stock?
- [ ] Registration table running smoothly?

**11:00 AM Check**
- [ ] Review sign-in sheet: count guests, tally school groups
- [ ] Report running total to Justin

**11:30 AM Check**
- [ ] Interest forms being distributed in all zones?
- [ ] Any material shortages?

**12:00 PM Check**
- [ ] Assist with media/photo coordination

**12:30 PM Check**
- [ ] Help announce "30 minutes remaining"
- [ ] Begin light cleanup (non-essential materials)

### Post-Event (1:00 PM - 2:00 PM)
- [ ] Collect ALL sign-in sheets (priority)
- [ ] Collect ALL interest forms from each zone
- [ ] Count guest attendance total
- [ ] Count interest forms (tally by grade level if possible)
- [ ] **VERIFY:** Token count from Zone 2 Lead
- [ ] **VERIFY:** Brochure/QR card distribution count
- [ ] Consolidate all data into summary sheet
- [ ] **DELIVER:** Complete count to Justin by 2:00 PM

### Success Metrics to Track
| Metric | Target | Actual |
|--------|--------|--------|
| Total Guests | 300-400 | _____ |
| Interest Forms | 50+ | _____ |
| Tokens Distributed | 200-250 | _____ |
| Brochures Distributed | 100-125 | _____ |
| School Groups | Track | _____ |

---

## 🎯 ZONE 1 LEAD - DESIGN LAB QUICK REF

**Station:** "Turn Code Into Products"  
**Duration:** 15-20 min per group | **Capacity:** 4-6 guests/group

### Essential Equipment
- [ ] Laptop powered (check connection)
- [ ] Projector displaying STL files
- [ ] Python scripts ready: `phase2/cad_design.py`
- [ ] USB backup drive connected
- [ ] Sample tokens displayed
- [ ] 30 "Try These Commands!" cheat sheets printed

### Key Demo (90-120 sec)
1. Explain Git: "Dropbox for code"
2. Show parametric design: Change gear teeth (20→30), see whole design update
3. Run: `python3 phase2/cad_design.py --shape gear --teeth 24 --diameter 60 --thickness 8`
4. Show physical token: "Your Python design became this real object"
5. Send to Zone 2

### Troubleshooting
- WiFi down? → Use USB backup
- Python error? → Switch to Laptop 2
- Guest confused? → Show the physical token (best visual proof)

### Photo Ops
- Guest at keyboard running code
- Code on screen + token next to it

---

## 🎯 ZONE 2 LEAD - LASER CUTTER QUICK REF

**Station:** "The Body - Watch Your Design Come to Life"  
**Duration:** 12-18 min per group | **Capacity:** 6-8 guests/group  
**⚠️ SAFETY CRITICAL - Follow procedures exactly**

### Pre-Demo Safety Briefing (MANDATORY)
> "No one closer than 3 feet while running. Don't look at beam. If fire alarm, evacuate. Understood?"

### Essential Equipment
- [ ] Laser cutter powered on & initialized
- [ ] G-code files loaded on control laptop
- [ ] 125 acrylic blanks in cutting bed (restock halfway)
- [ ] Ventilation fan ON (verify audible)
- [ ] Fire extinguisher accessible
- [ ] Tongs/heat-resistant gloves ready

### Key Demo (2-3 minutes)
1. Show design on screen (G-code)
2. Explain: "Laser vaporizes acrylic as it cuts"
3. Fire up laser - narrate the process
4. Remove token (after cooling) - hand to guest
5. Say: "Your code became this physical token"

### Troubleshooting
- Laser won't start? → Check door closed, E-stop position
- Cutting incomplete? → Check focal length
- **DON'T:** Run again until issue resolved (fire risk)

### Photo Ops
- Laser cutting in action (dramatic!)
- Token being held up (final product)

---

## 🎯 ZONE 3 LEAD - AUTONOMOUS SYSTEMS QUICK REF

**Station:** "The Brain - The Future of Robotics"  
**Duration:** 15-20 min per group | **Capacity:** 6-8 guests standing

### Essential Equipment
- [ ] Rover 1 powered on, SSH tested
- [ ] Rover 2 backup ready (full battery)
- [ ] Laptop connected to Rover 1
- [ ] Boundary markers in place (10'x10')
- [ ] Obstacle props ready (boxes, cones)
- [ ] 30 "Try These Commands!" cheat sheets printed

### Key Demo (4-5 min)
1. Intro: "These rovers think for themselves using sensors + code"
2. Show rover parts: wheels, ultrasonic sensor, Raspberry Pi, battery
3. Manual movement: `rover.move_north(50)` → Narrate
4. Obstacle demo: Place box → Rover stops automatically
5. Full course (if time): North→East→South→West→Home
6. Explain: "Same sensors power self-driving cars"

### Troubleshooting
- Rover won't respond? → Check SSH connection, Pi power
- Sensor reading wrong? → Recalibrate, move obstacle closer
- Battery dead? → Switch to Rover 2

### Photo Ops
- Rover moving (shows autonomy)
- Rover avoiding obstacle (shows intelligence)

---

## 📊 HOURLY SNAPSHOT - What Each Hour Looks Like

### 10:00 AM - START
- Zones open, first guest groups trickling in
- Zone Leads running initial demos
- Nicole managing registration table
- Justin observing all zones

### 10:30 AM - MOMENTUM BUILDING
- **CHECKPOINT:** Justin walks all zones (equipment status)
- Guests discovering zones
- Photo opportunities emerging
- Social media posts starting

### 11:00 AM - MID-EVENT PEAK
- **CHECKPOINT:** Attendance count (compare to target 150+ so far)
- Lines may start forming at popular zones
- Interest forms collecting
- Media may be arriving for interviews

### 11:30 AM - SUSTAIN PACE
- **CHECKPOINT:** Material supplies check (acrylic, tokens, forms)
- Peak hour of demo-running
- Staff energy: stay positive and energized
- Quality of each demo: still perfect

### 12:00 PM - MEDIA HOUR
- **CHECKPOINT:** Photos/video capture + interview window
- Highlight reel shots at each zone
- Justin available for media soundbites
- Quieter moment for photo staging

### 12:30 PM - FINAL PUSH
- **ANNOUNCEMENT:** "30 minutes remaining everyone!"
- Encourage interest form completion before leaving
- Last surge of guest flow
- Celebrate: "You're almost done! One more zone to check out"

### 1:00 PM - CLOSE
- Zones complete final demonstrations
- Begin controlled shutdown
- Guest exit countdown
- Thank guests at the door

### 1:00-2:00 PM - TEARDOWN
- Equipment powered down
- Materials collected/counted
- Sign-in sheets consolidated
- Preliminary data to Justin

---

## 🚨 EMERGENCY QUICK ACTIONS

| Situation | IMMEDIATE ACTION |
|-----------|------------------|
| **Fire alarm** | Evacuate immediately, all staff guide guests to exits |
| **Injury** | Alert Justin, call facility first aid, call 911 if serious |
| **Laser cutter fire** | Fire extinguisher at Zone 2; use if small; evacuate if large |
| **Rover malfunction** | Switch to Rover 2; call lead tech if Rover 2 fails |
| **Power outage** | Use laptop batteries; run non-tech demos (Zone 1 can talk through concepts) |
| **Extreme crowd** | Justin authorizes "quick view" mode (10-15 min instead of 20 min demos) |
| **Equipment failure** | Zone Leads: redirect guests; use backup equipment; notify Justin |

---

## 💬 KEY PHRASES TO USE

**Zone 1:** "You just designed a product. You're now an industrial designer."

**Zone 2:** "Digital design becomes physical reality in seconds."

**Zone 3:** "Same sensors power self-driving cars and Mars rovers."

**All Zones:** "Here's your token—proof you participated in the Detroit Automation Academy."

**To Guests:** "Take a picture with it—great for social media #DetroitAutomationAcademy"

---

## 📱 QUICK SCAN - What Success Looks Like at 1:00 PM

- **Attendance:** 300-400 guests signed in ✓
- **Interest Forms:** 50+ collected ✓
- **Tokens:** 200-250 distributed ✓
- **All Equipment:** Operational throughout ✓
- **No Major Incidents:** Zero safety violations ✓
- **Media:** 2-3 outlets covered event ✓
- **Staff Energy:** Team still smiling ✓
- **Guests Excited:** Positive feedback and energy ✓

**If most ✓:** EVENT SUCCESS! 🎉

---

## 📞 REACH JUSTIN IMMEDIATELY IF:
- Equipment fails (any zone)
- Guest injury or safety incident
- Severe crowd management issue
- Media emergency
- Attendance looking significantly different than projected

**Phone:** (313) 306-3767

---

**Last Updated:** February 3, 2026  
**Event Date:** February 4, 2026 | 10:00 AM - 1:00 PM  
**Status:** ✅ READY TO PRINT & DISTRIBUTE TO STAFF
