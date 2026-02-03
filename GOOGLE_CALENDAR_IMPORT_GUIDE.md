# 📅 GOOGLE CALENDAR IMPORT GUIDE
**Detroit Automation Academy - BGC Event Day 2**  
**Calendar File:** BGC_EVENT_DAY2_CALENDAR.ics  
**Date:** February 3, 2026

---

## 🚀 QUICK START - THREE IMPORT OPTIONS

### Option 1: Manual Import (Google Calendar Web)
**Easiest - No technical setup required**

1. Go to [Google Calendar](https://calendar.google.com)
2. Click **+ Create** → **Import & Export**
3. Select **"Import calendar"**
4. Upload `BGC_EVENT_DAY2_CALENDAR.ics`
5. Choose target calendar: **"Detroit Automation Academy"** or create new
6. Click **"Import"**

**Result:** All 3 events automatically added with attachments and attendees

---

### Option 2: Share Calendar Link
**Quick for team sharing**

1. Open Google Calendar
2. Go to **Settings** → **Calendars** → Select **Detroit Automation Academy**
3. Click **Share this calendar**
4. Add team members: Justin Smith, Nicole Yungers
5. Set permissions: **Editor** (for event management)
6. Manually attach the calendar file to meeting invites

---

### Option 3: Python API (Programmatic)
**For automated/repeated imports**

See `import_calendar_to_google.py` in this directory for automated import using Google Calendar API.

---

## 📋 PRE-IMPORT VERIFICATION

Before importing, verify the ICS file:

```bash
# Check file exists and has content
ls -lh BGC_EVENT_DAY2_CALENDAR.ics

# Verify structure (should show VCALENDAR and 3 VEVENT blocks)
grep -c "BEGIN:VEVENT" BGC_EVENT_DAY2_CALENDAR.ics  # Should output: 3
```

**Expected Output:**
```
3
```

If not 3 events, the file may be corrupted. Re-download from repository.

---

## ⚙️ DETAILED MANUAL IMPORT STEPS

### Step 1: Access Google Calendar
- Go to https://calendar.google.com
- Sign in with Detroit Automation Academy account
- Verify you're logged into the correct Google Workspace

### Step 2: Open Import/Export
- Click **Settings** (gear icon) → **Settings**
- Select **Import & Export** from left sidebar
- Scroll down to **"Import & Export"** section

### Step 3: Upload Calendar File
- Click **"Select file from your computer"**
- Navigate to `BGC_EVENT_DAY2_CALENDAR.ics`
- Select the file and click **"Open"**

### Step 4: Choose Target Calendar
- A dialog appears: "**Which calendar should these events be added to?**"
- Select: **"Detroit Automation Academy"** (if exists)
- OR click **"Create new calendar"** and name it: **"DAA Events"**

### Step 5: Confirm Import
- Click **"Import"** button
- Wait for confirmation: "**Calendar imported successfully**"

### Step 6: Verify Events Appear
- Check calendar for **February 4, 2026**
- Should see 3 events:
  - 9:00-10:00 AM: BGC Event Day 2 - Staff Setup & Briefing
  - 10:00 AM-1:00 PM: Boys & Girls Club Event - Day 2
  - 1:00-2:00 PM: BGC Event Day 2 - Teardown & Data Collection

### Step 7: Send Invitations
- Click on **main event** (10:00 AM - 1:00 PM)
- Click **"Edit event"**
- Click **"Add guests"**
- Add: justin.smith@detroitautomationacademy.org, nyungers@detroitautomationacademy.org
- Click **"Save"**
- Choose **"Notify guests"** when prompted
- Invitations sent automatically

---

## 📎 WHAT GETS IMPORTED

### Calendar Entries
- ✅ 3 events on February 4, 2026
- ✅ Correct times (with EST timezone)
- ✅ Location information
- ✅ Description text

### Event Details
- ✅ Event title and summary
- ✅ Start and end times
- ✅ Priority levels (High/Medium)
- ✅ Status (Confirmed)
- ✅ Categories (Education, Event, etc.)

### Attendee Information
- ✅ Justin Smith as organizer and attendee
- ✅ Nicole Yungers as attendee
- ✅ RSVP requests enabled
- ✅ Email notifications triggered

### Attachments
- ✅ Links to supporting documents (as calendar descriptions)
- ✅ Direct GitHub repository URLs
- ✅ Full document descriptions

---

## 🔄 AFTER IMPORT: NEXT STEPS

### Immediately After Import
1. **Verify attendance:** Check that invitations were sent to both attendees
2. **Test notifications:** Receive test notification from calendar
3. **Share calendar:** If not already shared, grant access to event staff

### February 3 (Today) - By 5:00 PM
4. **Collect RSVPs:** Follow up if Justin or Nicole haven't responded
5. **Print checklists:** Print `BGC_EVENT_DAY2_QUICK_CHECKLIST.md` for staff
6. **Distribute materials:** Email `STAFF_NOTIFICATION_BGC_DAY2.md` to all staff

### February 4 (Event Day)
7. **Reference calendar:** Use calendar notifications for hourly checkpoints
8. **Track attendance:** Use calendar attendee responses
9. **Update as needed:** Add notes/updates to calendar events

---

## ⚠️ TROUBLESHOOTING

### Issue: "Calendar import failed"
**Solution:**
- Verify ICS file is not corrupted
- Download fresh copy from GitHub
- Try importing to a different calendar first
- Check file size: Should be ~3-4 KB

### Issue: Events appear but times are wrong
**Solution:**
- Check Google Calendar timezone setting matches EST (-05:00)
- Settings → General → **Time Zone** → Set to "Eastern Time"
- Re-import if needed

### Issue: Attachments not showing
**Solution:**
- Attachments in ICS files appear as links in event description
- Click the GitHub URL in event description to access documents
- Verify GitHub access is not restricted

### Issue: Attendees not receiving invitations
**Solution:**
- Verify email addresses are correct:
  - Justin Smith: justin.smith@detroitautomationacademy.org
  - Nicole Yungers: nyungers@detroitautomationacademy.org
- Check spam folder for invitation emails
- Manually forward invitation link if needed

### Issue: Only 1-2 events imported (should be 3)
**Solution:**
- ICS file may be corrupted
- Delete imported events
- Download fresh file from GitHub repository
- Re-import

---

## 📊 SUCCESS INDICATORS

After successful import, you should see:

✅ **Calendar View**
- 3 events visible on Feb 4, 2026
- Color-coded events (typically purple/blue for events)
- Times visible in both day and week view

✅ **Event Details**
- Click any event and see:
  - Full description with event details
  - Location: Boys & Girls Club, Detroit, Michigan
  - Attendees listed with RSVP status
  - GitHub links to supporting documents

✅ **Attendee Invitations**
- Justin Smith: Invitation status shown
- Nicole Yungers: Invitation status shown
- RSVP responses tracked in calendar

✅ **Notifications**
- Calendar notifications configured
- Test notifications received

---

## 🔗 DOCUMENT REFERENCES

**Supporting Documents in Calendar:**

1. **BGC_EVENT_DAY2_SUMMARY.md** (Master Reference)
   - Link: https://github.com/smit4786/DetroitAutomationAcademy/blob/main/BGC_EVENT_DAY2_SUMMARY.md
   - Included in: All 3 events
   - Size: ~50 KB

2. **BGC_EVENT_DAY2_QUICK_CHECKLIST.md** (Field Reference)
   - Link: https://github.com/smit4786/DetroitAutomationAcademy/blob/main/BGC_EVENT_DAY2_QUICK_CHECKLIST.md
   - Included in: Events 1 & 2
   - Size: ~15 KB

3. **STAFF_NOTIFICATION_BGC_DAY2.md** (Staff Duties)
   - Link: https://github.com/smit4786/DetroitAutomationAcademy/blob/main/STAFF_NOTIFICATION_BGC_DAY2.md
   - Included in: Event 1 (Main Event)
   - Size: ~10 KB

4. **EVENT_PREP_SUMMARY.md** (Post-Event)
   - Link: https://github.com/smit4786/DetroitAutomationAcademy/blob/main/EVENT_PREP_SUMMARY.md
   - Included in: Event 3 (Teardown)
   - Size: ~10 KB

---

## 💡 BEST PRACTICES

### Calendar Management
- ✅ Use consistent timezone across all calendar entries
- ✅ Keep event descriptions detailed but concise
- ✅ Use color-coding: Red (urgent), Green (prep), Blue (event)
- ✅ Enable notifications 30 min and 1 day before event

### Attendee Management
- ✅ Send invitations at least 48 hours in advance ✓
- ✅ Include direct link to calendar event in email
- ✅ Follow up on RSVPs 24 hours before event
- ✅ Include alternative contact info in description

### Documentation
- ✅ Link all supporting materials in event descriptions
- ✅ Keep documents updated in repository
- ✅ Version control calendar exports
- ✅ Archive event calendar annually

### Post-Event
- ✅ Record actual attendance in event notes
- ✅ Update document with lessons learned
- ✅ Keep calendar event for historical reference
- ✅ Export calendar for annual report

---

## 📞 SUPPORT

**If import fails:**
1. Verify ICS file: `BGC_EVENT_DAY2_CALENDAR.ics` exists in workspace
2. Check Git repository: https://github.com/smit4786/DetroitAutomationAcademy
3. Re-download file if corrupted
4. Contact: Justin Smith (dbkrsmith+DAA@gmail.com)

**For Questions:**
- Event details: See BGC_EVENT_DAY2_SUMMARY.md
- Staff roles: See STAFF_NOTIFICATION_BGC_DAY2.md
- Field reference: See BGC_EVENT_DAY2_QUICK_CHECKLIST.md

---

## ✅ IMPORT CHECKLIST

- [ ] ICS file downloaded and verified
- [ ] Logged into Google Calendar with DAA account
- [ ] Calendar file successfully imported
- [ ] All 3 events visible on February 4
- [ ] Event times are correct (with EST timezone)
- [ ] Attendee emails added and visible
- [ ] Invitations sent to Justin Smith and Nicole Yungers
- [ ] Document attachments accessible via GitHub links
- [ ] Test notification received
- [ ] Event appears in team member's calendars

---

**Status:** ✅ **READY FOR IMPORT**

**Calendar File:** `BGC_EVENT_DAY2_CALENDAR.ics`  
**Location:** DetroitAutomationAcademy Repository  
**Format:** RFC 5545 ICS (standard calendar format)  
**Compatibility:** Google Calendar, Outlook, Apple Calendar, any ICS reader

**Import this calendar to activate all event notifications and attendee tracking.**

---

*Last Updated: February 3, 2026*  
*For: Detroit Automation Academy Leadership*
