# 🔳 QR Code Deployment: GitHub Issue Template

**Purpose:** Generate and deploy QR codes that direct students and families to the enrollment inquiry form  
**Target:** February 3-4, 2026 Boys & Girls Club event (and ongoing)  
**Status:** Ready for deployment  

---

## 📋 Overview

This directory contains QR code generation tools and deployment assets for the Detroit Automation Academy enrollment process. The QR codes encode links to the GitHub issue template, allowing guests at events to easily apply to the program.

### What is a QR Code?

A QR (Quick Response) code is a 2D barcode that stores information—in this case, a URL. When scanned with a smartphone camera or QR code reader, it opens the enrollment link instantly.

### Why QR Codes?

- ✅ **No typing required** - Guests don't need to remember domain names or search for the link
- ✅ **Frictionless** - One tap from any smartphone
- ✅ **Trackable** - We can monitor how many scans occur at the event
- ✅ **Versatile** - Can be printed on posters, signs, business cards, or digital displays

---

## 🚀 Quick Start

### 1. Generate QR Codes

```bash
cd /Users/jsmith34/Documents/gitHub/DetroitAutomationAcademy

# Generate all formats (PNG, SVG, PDF) for all sizes
python3 generate_qr_codes.py --all-configs

# Or generate specific format
python3 generate_qr_codes.py --format png --size 10
```

**Output:** Creates `qr_codes/` directory with files like:
- `enrollment_qr_poster_*.png` - Large format (posters)
- `enrollment_qr_sign_*.png` - Medium format (event signs)
- `enrollment_qr_card_*.png` - Small format (business cards)
- `enrollment_qr_social_*.png` - Social media format
- `enrollment_qr_*.svg` - Vector format (highest quality)
- `enrollment_qr_*.pdf` - Print-ready

### 2. Print QR Codes

For the **February 3-4 event**, we need:

| Format | Quantity | Size | Use Case |
|--------|----------|------|----------|
| **Posters** | 5 | 36" × 24" | Event entrance, each zone |
| **Signs** | 10 | 24" × 18" | Table signs, directional markers |
| **Cards** | 500 | 3.5" × 2" | Handouts to guests |
| **Social** | Digital | 1200×630px | Instagram, Facebook, email |

### 3. Test the QR Codes

Before printing, verify each QR code works:

1. **On your smartphone:**
   - Open camera app or QR code reader
   - Point at printed/digital QR code
   - Tap notification to open link
   - Verify it opens: `https://github.com/smit4786/DetroitAutomationAcademy/issues/new?template=enrollment-inquiry.md`

2. **Online:**
   - Use online QR code validators
   - Search "QR code scanner online"
   - Upload PNG file to verify

---

## 📍 Deployment Locations

### Event Locations (Feb 3-4)

| Location | QR Code Format | Quantity | Purpose |
|----------|---|---|---|
| **Event Entrance** | Poster (36"×24") | 2 | Main visibility |
| **Zone 1 (Design Lab)** | Sign (24"×18") + Cards | 2 + 50 | Students, software demo |
| **Zone 2 (Rapid Prototyping)** | Sign + Cards | 2 + 100 | Token distribution area |
| **Zone 3 (Autonomous Systems)** | Sign + Cards | 2 + 100 | Rover demo area |
| **Registration Table** | Sign + Cards | 2 + 200 | Primary application point |

### Digital Deployment

| Channel | Format | Action |
|---------|--------|--------|
| **Social Media** | PNG (1200×630px) | Post on Instagram, Facebook, Twitter |
| **Email Campaign** | PNG or SVG | Include in email blast to families |
| **Website** | SVG (vector) | Embed on application page |
| **Slack/Discord** | PNG | Share with student and parent groups |

---

## 🎨 Design Specifications

### Color Palette

All QR codes use Detroit Automation Academy brand colors:

- **Primary Module Color:** `#0066CC` (Electric Blue)
- **Background:** `#FFFFFF` (White)
- **Alternative (Monochrome):** `#000000` (Black on white)

### Size Guidelines

| Use Case | Size | Resolution | Print Quality |
|----------|------|-----------|--|
| Poster | 36" × 24" | 300 DPI minimum | Professional |
| Event Sign | 24" × 18" | 300 DPI minimum | Professional |
| Business Card | 3.5" × 2" | 300 DPI minimum | High quality |
| Digital Display | 1200 × 630px | 72 DPI | Web standard |
| Email | 600 × 600px | 72 DPI | Mobile-friendly |

### Error Correction

All generated QR codes use **Level H error correction** (30% data recovery), ensuring codes remain scannable even if:
- 30% of the code is damaged or obscured
- Code is partially torn or faded
- Code is partially covered by debris

---

## 🔗 URL Encoding

### GitHub Issue Template URL

The QR codes encode the following link:

```
https://github.com/smit4786/DetroitAutomationAcademy/issues/new?template=enrollment-inquiry.md
```

**What this does:**
1. Opens the Detroit Automation Academy GitHub repository
2. Initiates creation of a new issue
3. Pre-fills the issue form with the enrollment inquiry template (see [ISSUE_TEMPLATE/enrollment-inquiry.md](../ISSUE_TEMPLATE/enrollment-inquiry.md))
4. Students fill in their contact info, program interest, and availability

### Alternative URLs (Future Use)

Once we deploy a custom web application, we can update QR codes to point to:

```
https://detroitautomationacademy.org/apply
```

Update the `APPLICATION_PORTAL_URL` variable in `generate_qr_codes.py` and regenerate.

---

## 📊 Tracking QR Code Scans

### GitHub-Based Tracking

GitHub provides basic analytics:

1. Open repository settings
2. Go to "Insights" → "Traffic"
3. View "Referrers" to see external link sources
4. Monitor issue creation rate during event

### URL Shortener Tracking (Optional)

For more detailed analytics, create a shortened URL with tracking:

```bash
# Using bit.ly or TinyURL
# Visit: https://bitly.com
# Create custom short URL pointing to:
# https://github.com/smit4786/DetroitAutomationAcademy/issues/new?template=enrollment-inquiry.md
# Then encode SHORT URL in QR code instead

# Example: bit.ly/daa-enroll
```

**Advantage:** Detailed click-through statistics, geography, device type  
**Disadvantage:** Requires third-party service

---

## 🛠️ Advanced: Customizing QR Codes

### Generate for Specific Use Case

```bash
# Poster size (large)
python3 generate_qr_codes.py --config poster

# Business card size (small)
python3 generate_qr_codes.py --config card

# All configurations at once
python3 generate_qr_codes.py --all-configs
```

### Custom Colors (Advanced)

Edit `generate_qr_codes.py` and modify the `QR_CONFIGS` dictionary:

```python
QR_CONFIGS = {
    "custom": {
        "size": 12,
        "border": 3,
        "fill_color": "#FF6B35",      # Change to your color (hex)
        "back_color": "#FFFBF0",      # Background color
        "description": "Custom branding",
    }
}
```

### Generate for Different URL

```bash
python3 generate_qr_codes.py --url "https://your-url-here.com"
```

---

## 📋 Printing Instructions

### For Print Shop

1. **File Format:** Use `.pdf` or `.svg` files (vector formats)
2. **Resolution:** Ensure 300 DPI minimum
3. **Color Mode:** RGB or CMYK (both work)
4. **Material:** Matte or glossy paper (both scannable)
5. **Quantity:** See [Deployment Locations](#deployment-locations) section

### DIY Printing

1. **Printer Settings:**
   - Color: Full color (or black & white monochrome)
   - Paper type: Standard copy paper or cardstock
   - DPI: 300 DPI if available
   - Scale: Do NOT scale to fit (maintain original dimensions)

2. **Quality Check:**
   - Test scan each printed QR code before distributing
   - Ensure no ink smudging or misalignment
   - Verify contrast between modules and background

---

## ⚠️ Troubleshooting

### QR Code Won't Scan

**Symptoms:** Smartphone camera/QR reader fails to recognize code

**Solutions:**
1. Ensure sufficient contrast (dark modules on light background)
2. Check code hasn't faded or been damaged
3. Try different QR scanner app (some are more robust)
4. Ensure adequate lighting (not too dark or glary)
5. Hold scanner 4-8 inches away from code

### QR Code Scans to Wrong URL

**Symptoms:** QR code opens unexpected link

**Solution:** Regenerate using correct URL:
```bash
python3 generate_qr_codes.py --url "https://correct-url.com"
```

### URL Too Long / QR Code Too Complex

**Symptoms:** Generated QR code is very dense, hard to scan

**Solution:** Use URL shortener:
1. Visit [bit.ly](https://bitly.com) or [TinyURL](https://tinyurl.com)
2. Create short link for enrollment URL
3. Regenerate QR code with short URL

---

## 📱 Testing Checklist

- [ ] Generate all QR code formats
- [ ] Test each PNG file with smartphone camera app
- [ ] Verify QR code opens correct GitHub issue template
- [ ] Check that issue template pre-fills correctly
- [ ] Print test versions on regular and cardstock paper
- [ ] Scan printed versions to verify image quality
- [ ] Test from different distances (4", 12", 24")
- [ ] Test in various lighting conditions
- [ ] Share digital versions on social media
- [ ] Monitor GitHub issue creation during event

---

## 📚 Integration with Event Materials

### Update Event Checklist

The QR codes should be referenced in [EVENT_CHECKLIST_FIXED.md](../instructor_resources/event_checklists/EVENT_CHECKLIST_FIXED.md):

**Add to PRE-EVENT CHECKLIST:**
```
#### QR Code Signage
- [ ] 5 Poster QR codes (36" × 24") printed and ready
- [ ] 10 Event sign QR codes (24" × 18") printed and ready
- [ ] 500 Business card QR codes (3.5" × 2") printed and assembled
- [ ] QR code scanning tested on 3+ smartphone models
- [ ] Backup digital QR codes loaded on display screens
```

### Update Zone Scripts

Add to each zone script ([ZONE_1_DESIGN_LAB.md](../instructor_resources/zone_scripts/ZONE_1_DESIGN_LAB.md), etc.):

```markdown
### QR Code Information

**"If you're interested, grab an interest form on your way out, or scan this QR code to apply when our application portal opens February 7th."**

[Point to QR code poster or registration table]
```

### Update Event Guide

Add to [bgc_event_guide.md](../docs/bgc_event_guide.md):

```markdown
### QR Code Distribution
- Station 1: 50 business card QR codes
- Station 2: 150 business card QR codes  
- Station 3: 100 business card QR codes
- Registration table: 150 business card QR codes
- Event entrance: 2 large poster QR codes
```

---

## 🚀 Deployment Timeline

| Date | Task | Owner |
|------|------|-------|
| **Jan 27** | Generate all QR code formats | @CTO |
| **Jan 30** | Submit to print shop (posters, signs, cards) | @Admin |
| **Feb 1** | Receive printed materials | @Admin |
| **Feb 2** | QA check all printed codes (scan test) | @Event-Team |
| **Feb 3-4** | Deploy at event (5 posters, 10 signs, 500 cards) | @Event-Staff |
| **Post-Event** | Monitor GitHub issue creation analytics | @Admin |

---

## 📞 Support & Questions

If you encounter issues:

1. **For printing questions:** Contact your print shop
2. **For QR code generation:** Check troubleshooting section above
3. **For GitHub integration:** See [@CTO Technical Roadmap](../CTO_TECHNICAL_ROADMAP.md)
4. **For event logistics:** Contact @Admin or @Event-Coordinator

---

## 📄 Related Documents

- [Event Checklist](../instructor_resources/event_checklists/EVENT_CHECKLIST_FIXED.md)
- [Zone Scripts](../instructor_resources/zone_scripts/)
- [Issue Template](../ISSUE_TEMPLATE/enrollment-inquiry.md)
- [Event Guide](../docs/bgc_event_guide.md)
- [GitHub Repository](https://github.com/smit4786/DetroitAutomationAcademy)

---

**QR Code Deployment Status:** ✅ **Ready for production**

**Last Updated:** February 3, 2026  
**Owner:** @CTO / @Admin  
**Next Review:** Post-event analytics (February 5, 2026)
