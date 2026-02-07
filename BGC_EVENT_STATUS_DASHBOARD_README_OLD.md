# 📊 BGC Event Status Dashboard - Quick Setup Guide

**File:** `BGC_EVENT_STATUS_DASHBOARD.html`  
**Event Date:** February 4, 2026  
**Purpose:** Real-time student signup tracking via GitHub Issues

---

## 🚀 Quick Start (3 Methods)

### Method 1: Open Locally (Easiest)
1. Double-click `BGC_EVENT_STATUS_DASHBOARD.html`
2. Opens in your default browser
3. **Works immediately** - no server needed!

### Method 2: Run with Python Server
```bash
# In the repository root directory:
cd /Users/jsmith34/Documents/gitHub/DetroitAutomationAcademy
python3 -m http.server 8080

# Open in browser:
# http://localhost:8080/BGC_EVENT_STATUS_DASHBOARD.html
```

### Method 3: Deploy to GitHub Pages
1. Push the file to GitHub
2. Enable GitHub Pages in repository settings
3. Access at: `https://smit4786.github.io/DetroitAutomationAcademy/BGC_EVENT_STATUS_DASHBOARD.html`

---

## 📱 Display Setup at Event

### Recommended Hardware
- **Tablet:** iPad Pro 12.9" or similar (landscape mode)
- **Monitor:** Any 24"+ display with HDMI connection
- **Stand:** Positioned next to QR code signage for maximum visibility

### Browser Setup
1. Open dashboard in Chrome, Firefox, or Safari
2. Press `F` key to enter **fullscreen mode**
3. Ensure Wi-Fi connection is stable
4. Let it run - auto-refreshes every 30 seconds!

### Positioning Strategy
```
┌──────────────────┐     ┌─────────────────────┐
│   QR CODE SIGN   │ <-> │  STATUS DASHBOARD   │
│  (Print Poster)  │     │   (Live Tablet)     │
│                  │     │                     │
│  [QR CODE HERE]  │     │ Total Signups: 12   │
│                  │     │ This Hour: 4        │
│  "Scan to Join!" │     │ Recent: Alice, Bob  │
└──────────────────┘     └─────────────────────┘
       ↓                           ↓
   [Students scan]         [See real-time updates]
```

---

## 🎯 What It Displays

### Top Metrics (4 Cards)
1. **Total Registrations** - All enrollment issues created
2. **QR Scans (Estimated)** - Based on 30% completion rate
3. **Conversion Rate** - Percentage who completed after scanning
4. **Last Updated** - Most recent data refresh timestamp

### Main Content Area
- **Recent Enrollments** (left) - Scrollable list of all submissions
- **This Hour** (right) - Current hour signup count
- **Peak Hour** (right) - Highest signups in any single hour
- **Signups by Hour** (right) - Visual bar chart (10 AM - 1 PM)

### Quick Links (Footer)
- 📋 View All Issues (GitHub)
- 📝 Enrollment Template (GitHub)
- 📱 QR Code Image (local file)

---

## ⚙️ How It Works

### GitHub Integration
- Fetches issues from: `https://github.com/smit4786/DetroitAutomationAcademy`
- Filters by label: `enrollment`
- Shows both **open** and **closed** issues
- **No authentication required** for public repos

### Auto-Refresh
- Updates every **30 seconds** automatically
- Press `R` key to manually refresh anytime
- Green indicator dot shows active refresh status

### Real-Time Tracking
When a student:
1. Scans QR code → Opens GitHub issue template
2. Fills out enrollment form → Creates new issue with `enrollment` label
3. Submits → **Appears on dashboard within 30 seconds!** ✨

---

## 🎨 Branding (DAA Colors)

The dashboard uses official Detroit Automation Academy branding:

| Element | Color | Hex Code |
|---------|-------|----------|
| Primary (headers, metrics) | Electric Blue | `#0066CC` |
| Accent (highlights) | Rust / Detroit Burn | `#CC5522` |
| Success (conversion rate) | Lime / Forward Motion | `#66CC00` |
| Typography | Poppins (display), Inter (body) | Google Fonts |

---

## 🔧 Troubleshooting

### Issue: Dashboard shows "0 registrations"
**Solution:** 
- Check internet connection
- Verify GitHub repo is public: `https://github.com/smit4786/DetroitAutomationAcademy`
- Confirm issues have the `enrollment` label

### Issue: Data not refreshing
**Solution:**
- Press `R` key to force refresh
- Check browser console (F12) for errors
- Ensure GitHub API isn't rate-limited (60 requests/hour for unauthenticated)

### Issue: "GitHub API Error"
**Solution:**
- Check if repository exists and is public
- Verify owner/repo names in code: `smit4786/DetroitAutomationAcademy`
- For private repos, add GitHub token (see "Advanced Configuration" below)

### Issue: Tablet screen turns off
**Solution:**
- Disable auto-sleep in device settings
- Keep tablet plugged into power
- Use browser extension to prevent screen timeout

---

## 🔐 Advanced Configuration

### For Private Repositories
If your repo is private, add a GitHub Personal Access Token:

1. Generate token at: https://github.com/settings/tokens
2. Permissions needed: `repo` (read access)
3. Edit line 569 in the HTML file:
```javascript
headers: {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token YOUR_GITHUB_TOKEN_HERE'  // Add this line
}
```

### Change Refresh Interval
Default: 30 seconds. To change:
```javascript
// Line 547 - Change refreshInterval value
const GITHUB_CONFIG = {
    owner: 'smit4786',
    repo: 'DetroitAutomationAcademy',
    label: 'enrollment',
    apiBase: 'https://api.github.com',
    refreshInterval: 15000  // 15 seconds (or any milliseconds value)
};
```

### Change Repository/Label
```javascript
// Line 547-549
owner: 'YOUR_GITHUB_USERNAME',
repo: 'YOUR_REPO_NAME',
label: 'YOUR_LABEL_NAME',
```

---

## 📋 Pre-Event Checklist

- [ ] Test dashboard on actual display device (tablet/monitor)
- [ ] Verify GitHub issues are being created with `enrollment` label
- [ ] Test QR code → form → issue creation workflow
- [ ] Disable screen timeout on display device
- [ ] Ensure stable Wi-Fi connection at venue
- [ ] Position dashboard next to QR code signage
- [ ] Brief staff on keyboard shortcuts (R = refresh, F = fullscreen)
- [ ] Have backup plan (mobile hotspot) if venue Wi-Fi fails

---

## 🎓 Event Day Tips

### For Staff
1. **Arrival:** Set up dashboard 30 minutes before event
2. **Testing:** Create test enrollment issue to verify display
3. **Monitoring:** Glance periodically to ensure data is updating
4. **Engagement:** Point students to dashboard to see their submission appear!

### For Students
- **Excitement:** "Your name will appear on the screen within 30 seconds!"
- **Verification:** Students can see their submission immediately
- **Social Proof:** Others can see real-time signups happening

---

## 📊 Expected Metrics (Based on Planning Docs)

| Metric | Target | Calculation |
|--------|--------|-------------|
| Total Attendees | 300-400 | Event capacity |
| QR Scans | 100-150 | ~35% of attendees |
| Form Completions | 50+ | ~30% completion rate |
| Conversion Rate | 30-50% | Completions / Scans |
| Peak Hour | 11:00 AM | Mid-event |

---

## 🎉 Post-Event Actions

1. **Screenshot Dashboard** - Document final metrics
2. **Export GitHub Issues** - Download CSV of all enrollments
3. **Follow-Up** - Email accepted students within 48 hours
4. **Analysis** - Review conversion rate and peak times for future events

---

## 📞 Support

**Technical Issues During Event:**
- Justin Smith (Founder & Lead Technologist)
- Reference: `BGC_EVENT_DAY2_SUMMARY.md`

**GitHub Integration:**
- Repository: https://github.com/smit4786/DetroitAutomationAcademy
- Issues: https://github.com/smit4786/DetroitAutomationAcademy/issues

**Quick Reference Docs:**
- `QR_CODE_QUICK_REFERENCE.md` - QR code setup
- `TEMPLATE_ENROLLMENT_FORM.md` - Form structure
- `BGC_EVENT_DAY2_QUICK_CHECKLIST.md` - Event logistics

---

## ✅ Features Checklist

- [x] Real-time GitHub Issues integration
- [x] Auto-refresh every 30 seconds
- [x] DAA branding (colors, fonts)
- [x] Responsive design (mobile, tablet, desktop)
- [x] No external dependencies (pure HTML/CSS/JS)
- [x] Works locally or via GitHub Pages
- [x] Hourly breakdown visualization
- [x] Conversion rate tracking
- [x] Quick links to resources
- [x] Keyboard shortcuts (R = refresh, F = fullscreen)
- [x] Error handling and loading states
- [x] Accessibility (WCAG AA contrast ratios)

---

**Version 1.0** | Created February 3, 2026 | Detroit Automation Academy  
**Next Event:** Boys & Girls Club | February 4, 2026 | 10:00 AM - 1:00 PM

🚀 **Good luck with the event!**
