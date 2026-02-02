# 🖥️ ZONE 1 SCRIPT: DESIGN LAB (SOFTWARE & GIT)
## Student Assistant Guide - February 3-4, 2025

**Station Name:** "Design Lab - Turn Code Into Products"  
**Duration per guest group:** 15-20 minutes  
**Key Skill:** Explaining how Python code becomes physical designs  

---

## 🎯 OPENING SCRIPT (Greeting)

**[Smile, make eye contact, gesture to station]**

**"Hi, welcome to the Design Lab! I'm _________, and I'm going to show you something really cool—how we use Python code to design physical products.**

**Have you ever used Git or Python before? No worries if you haven't—we'll walk through it together. This is the first step in turning an idea into a product that you could actually build with a laser cutter or 3D printer. Ready?"**

---

## 📋 DEMO WALKTHROUGH (Step-by-Step)

### Step 1: Explain Git (60 seconds)
**[Point to laptop screen]**

**"So this is called Git. It's like Dropbox, but for code. Imagine you and a friend are both working on a project—Git keeps track of who changed what, and when. This is called 'version control.'**

**Our Detroit Automation Academy curriculum is actually stored on GitHub—that's a website that hosts code repositories. So when we run this command..."**

**[Type or highlight on screen: `git clone https://github.com/smit4786/detroit-automation-academy.git`]**

**"...we're downloading all our course materials to this laptop. Pretty neat, right?"**

### Step 2: Parametric Design Concept (90 seconds)
**[Open a pre-generated STL file in 3D viewer OR show Python script on screen]**

**"Okay, so here's the magic part. This is a gear—you know, like the metal part in a clock or a robot? Here's how we designed it:**

**In Python, we write instructions like: 'Make a gear with 20 teeth, 50mm diameter, 5mm thickness.' Then the computer generates the exact 3D shape.**

**But here's the cool part—if we change just ONE number, say we want 30 teeth instead of 20, the whole design updates automatically."**

**[If time, show changing a parameter on screen]**

**"That's called 'parametric design.' Instead of drawing every tooth by hand, we let code do the heavy lifting. This is exactly how engineers at companies like Tesla and SpaceX design parts."**

### Step 3: Generate Custom Gear (90-120 seconds)
**[Bring guest to keyboard or prepare pre-command-executed result]**

**"Now you try. We're going to run a command to generate a custom gear. Here's the command:"**

**[Point to typed or printed command:]**
```
python3 phase2/cad_design.py --shape gear --teeth 24 --diameter 60 --thickness 8
```

**"What this says is: 'Hey Python, generate a gear with these exact specs.' Let's press Enter and see what happens..."**

**[Hit Enter OR show pre-generated result]**

**"Boom! There's your gear. This file is called an STL file—that's the format 3D printers and laser cutters understand. In about 10 seconds, this exact gear will be cut by the laser cutter in the next zone."**

### Step 4: Show The Real Token (60 seconds)
**[Hold up a laser-cut token from Zone 2]**

**"See this token? This is what we're cutting right now in Zone 2. It was designed exactly like this—someone wrote Python code, generated the STL file, and then sent it to the laser cutter.**

**This token is your proof that you participated. And if you look at the back, you'll see it has today's date and 'Detroit Automation Academy' engraved on it."**

**[Pass token to guest to hold]**

**"Pretty cool, right? You just designed a product. You're basically an industrial designer now."**

---

## 💬 KEY TALKING POINTS (If Asked Questions)

### "What's Git actually used for?"
**"Git is used by companies like Google, Facebook, and Microsoft. Thousands of programmers can work on the same project, and Git makes sure nobody overwrites someone else's work. It's essential in the tech industry."**

### "Why Python?"
**"Python is one of the easiest programming languages to learn, but it's also powerful enough for real industrial work. Companies like NASA use Python for robotics, and so do we."**

### "Can we design other shapes?"
**"Absolutely! In our full program, students design gears, brackets, wheels, robot chassis—basically anything. The tools work the same way: write code, generate geometry, send to 3D printer or laser."**

### "How long does this take in real work?"
**"Depends on the complexity, but often just minutes. An engineer at Tesla might design a bracket in Python, test it with simulation software, then 3D print a prototype within an hour. That's the power of automation."**

### "Do I need to be good at math?"
**"Not really. You need basic geometry (circles, rectangles, triangles), and Python handles the hard stuff. The creativity is the most important part—what do you WANT to design?"**

---

## 🆘 TROUBLESHOOTING GUIDE

### Problem: WiFi Is Down
**Solution:**
- [ ] Locate USB backup drive (should be taped to monitor)
- [ ] Open file browser, navigate to `/phase2/cad_design.py`
- [ ] Run the same command from the USB drive
- [ ] If that fails, show pre-generated STL file from backup folder
- **Say to guest:** "We had a WiFi hiccup, but that's why we have backups. Let me show you the same result..."

### Problem: Python Script Won't Run
**Solution:**
- [ ] Check if Python 3.9+ is installed: `python3 --version`
- [ ] Check if required libraries are installed: `pip3 list | grep pandas`
- [ ] If library missing, say: "Let me switch to Laptop 2, which has everything set up"
- **Do NOT try to debug live with guest present—switch devices**

### Problem: Guest Doesn't Understand Git
**Solution:**
- [ ] Use simpler analogy: "Git is like 'Save As' on Microsoft Word, but for code"
- [ ] Skip deep explanation, focus on the *result*: "We download the code, run this command, and boom—custom design"
- [ ] Show the token instead: "Here's what the code created"

### Problem: Projector Isn't Displaying
**Solution:**
- [ ] Check HDMI cable (swap for backup if available)
- [ ] Check laptop display settings (might be mirrored to external display only)
- [ ] If unfixable, gather guests around laptop screen instead
- [ ] Call Lead Instructor for help

### Problem: Guest Wants To Try Typing Commands
**Solution:**
- [ ] Great! Let them (if time permits, 3-5 min)
- [ ] Guide their fingers to the keys: "Try typing: `python3 --version`"
- [ ] Celebrate when command runs: "You just ran a Python command! That's coding!"
- [ ] If it fails, don't make guest feel bad—offer to show on your keyboard instead

---

## 📸 PHOTO OPPORTUNITIES

**Good shots for media kit:**
- Student pointing at code on screen
- Guest at keyboard running command
- Close-up of STL file on 3D viewer
- Student holding token next to laptop showing the code

**Say to guest:** "Hey, mind if we get a quick photo? We're creating a media kit to show what we do here."

---

## 🔄 CLOSING SCRIPT

**[As time runs out, stand up and gesture toward next zone]**

**"So that's the Design Lab—Python code becomes geometry becomes physical products. Next, you're heading to the 'Rapid Prototyping' zone where you'll see the laser cutter in action. It's going to cut this exact design we just made into your commemorative token. Pretty awesome, right?**

**Thanks for coming by! Any last questions before you head over?"**

**[If questions, answer briefly. If not:]**

**"Awesome! Have fun at the next zone, and grab your token on the way out. See you later!"**

---

## 📝 NOTES FOR STUDENT ASSISTANTS

- **Confidence is key.** You don't need to be a programmer to explain this—just follow the script and show enthusiasm
- **Watch for confusion.** If guest's eyes glaze over, switch to showing the token instead of explaining Git
- **Keep it snappy.** 15-20 min max. If you go over 20 min, other guests are waiting
- **Have the USB backup ready** (taped to monitor)
- **Know where everything is:** Laptop 1, Laptop 2, Laptop 3, USB drive, projector, power cords
- **If anything breaks,** call the Lead Instructor (not assigned to a zone = roaming troubleshooter)

---

**Questions before the event? Ask your Lead Instructor during the Feb 2 rehearsal.**

**You've got this! 🚀**
