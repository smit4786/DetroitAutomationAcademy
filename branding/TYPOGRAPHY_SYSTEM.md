# 🔤 TYPOGRAPHY SYSTEM - Detroit Automation Academy

**Document Version:** 1.0  
**Date:** January 31, 2026  
**Status:** Phase 1 - Typography Definition  
**Owner:** @CTO  
**Deadline:** Feb 3, 2026 (Final selection approved)

---

## 📚 TYPOGRAPHY STRATEGY

Detroit Automation Academy's typography system should communicate:
- **Modern professionalism** (suitable for grants and corporate partnerships)
- **Accessibility and clarity** (readable for all users)
- **Human-centered warmth** (not cold or corporate)
- **Tech credibility** (contemporary, forward-thinking)
- **Versatility** (works web, print, merchandise)

---

## 🔤 THREE-FONT STRATEGY

### Font Role 1: DISPLAY / HEADING FONT
**Purpose:** Logo text, major headings (H1), key callouts, branding elements

**Requirements:**
- ✅ Strong, distinctive personality
- ✅ Professional and modern
- ✅ Highly legible at large sizes
- ✅ Works well with logo
- ✅ Available in multiple weights (bold minimum)

**Candidate Options:**

**Option 1A: Poppins (Google Fonts, Free)**
- **Category:** Geometric sans-serif
- **Best For:** Modern, friendly, tech-forward
- **Weights Available:** 100-900 (all weights free)
- **Pairing:** Works well with clean body font
- **Pros:** Free, professional, modern, geometric feel
- **Cons:** Very popular (less distinctive)
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&display=swap');
font-family: 'Poppins', sans-serif;
```

**Option 1B: Inter (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Modern professional, accessible
- **Weights Available:** 100-900 (all free)
- **Pairing:** Excellent with itself for body text
- **Pros:** Extremely legible, modern, professional, excellent metrics
- **Cons:** Less distinctive personality
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;800&display=swap');
font-family: 'Inter', sans-serif;
```

**Option 1C: Raleway (Google Fonts, Free)**
- **Category:** Geometric sans-serif
- **Best For:** Elegant, modern, distinctive
- **Weights Available:** 100-900 (all free)
- **Pairing:** Good with humanist body fonts
- **Pros:** Elegant geometric style, distinctive, free
- **Cons:** Thinner weights less suitable for body text
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@700;800&display=swap');
font-family: 'Raleway', sans-serif;
```

**Option 1D: Work Sans (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Technical, professional, clean
- **Weights Available:** 100-900 (all free)
- **Pairing:** Pairs well with technical body fonts
- **Pros:** Professional tech feel, clean, modern
- **Cons:** Less distinctive personality
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@700;800&display=swap');
font-family: 'Work Sans', sans-serif;
```

**PRELIMINARY RECOMMENDATION:** **Poppins**
- Modern and distinctive without being trendy
- Excellent legibility at display sizes
- Strong personality that suits tech/education
- Geometric feel complements "gear" logo concepts
- Completely free with excellent language support

---

### Font Role 2: BODY TEXT FONT
**Purpose:** Paragraph text, documentation, long-form content, accessibility

**Requirements:**
- ✅ Highly readable (large x-height, clear letterforms)
- ✅ Professional appearance
- ✅ Optimized for screen reading (generous spacing)
- ✅ Multiple weights available (regular, semibold, bold)
- ✅ Excellent hinting for web rendering

**Candidate Options:**

**Option 2A: Inter (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Web, accessibility, screen readability
- **Weights Available:** 100-900
- **Line Height:** Excellent metrics built-in
- **Pros:** Best-in-class web rendering, accessible, open-source
- **Cons:** Less personality (neutral is good for body text)
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
font-family: 'Inter', sans-serif;
line-height: 1.6;
```

**Option 2B: Source Sans Pro (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Professional, highly legible, versatile
- **Weights Available:** 200-900
- **Line Height:** Excellent readability
- **Pros:** Adobe font (professional standard), highly legible, free on Google Fonts
- **Cons:** Slightly heavier files
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&display=swap');
font-family: 'Source Sans Pro', sans-serif;
```

**Option 2C: Lato (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Warm, accessible, friendly
- **Weights Available:** 100-900
- **Line Height:** Good readability with warm feel
- **Pros:** Warm and approachable, excellent for education, free
- **Cons:** Slightly less modern than Inter
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;600;700&display=swap');
font-family: 'Lato', sans-serif;
```

**Option 2D: IBM Plex Sans (Google Fonts, Free)**
- **Category:** Humanist sans-serif
- **Best For:** Technical, professional, systematic
- **Weights Available:** 100-700
- **Line Height:** Excellent tech documentation feel
- **Pros:** IBM professional standard, technical credibility, free
- **Cons:** Slightly technical feel (good for DAA!)
- **License:** Open Font License (OFL)

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap');
font-family: 'IBM Plex Sans', sans-serif;
```

**PRELIMINARY RECOMMENDATION:** **Inter**
- Best web rendering and accessibility
- Pairs perfectly with Poppins (geometric + humanist)
- Excellent readability on all devices
- Professional and modern
- Completely free with excellent language support

---

### Font Role 3: ACCENT / LOGO FONT
**Purpose:** Logo treatment, special emphasis, distinctive markers

**Options:**

**Option 3A: Use Heading Font (Poppins)**
- **Advantage:** Cohesive, simple, professional
- **Disadvantage:** Less distinctive logo treatment
- **Recommendation:** Start here, evolve to custom if needed

**Option 3B: Custom Letterforms**
- **Advantage:** Unique, ownable, distinctive
- **Disadvantage:** Expensive ($500-$2,000 for custom)
- **Recommendation:** Consider for future evolution

**Option 3C: License Distinctive Font (Premium)**
- **Cost:** $100-$500 per license
- **Advantage:** Professional, distinctive, properly licensed
- **Examples:** Futura, DIN, Gotham, Circular
- **Recommendation:** Future enhancement if budget allows

**PRELIMINARY RECOMMENDATION:** **Use Poppins Bold** for logo
- Cost-effective (free)
- Distinctive geometric treatment
- Professional and modern
- Can evolve to custom letterforms later if desired

---

## 📐 TYPOGRAPHY SPECIFICATIONS

### Heading Hierarchy

**H1 (Logo/Display Headlines)**
- Font: Poppins Bold (800)
- Size: 48-64px (desktop), 32-40px (mobile)
- Line Height: 1.2
- Letter Spacing: -0.02em
- Color: Primary brand color (blue)
- Use: Page titles, major section headings

**H2 (Section Headings)**
- Font: Poppins Bold (700)
- Size: 32-40px (desktop), 24-28px (mobile)
- Line Height: 1.3
- Letter Spacing: -0.01em
- Color: Primary brand color or Black
- Use: Main section headings, subsection headers

**H3 (Subsection Headings)**
- Font: Poppins SemiBold (600)
- Size: 20-28px (desktop), 18-22px (mobile)
- Line Height: 1.4
- Letter Spacing: 0em
- Color: Dark gray or black
- Use: Subsection headers, category titles

**H4/H5 (Minor Headings)**
- Font: Inter SemiBold (600)
- Size: 16-20px
- Line Height: 1.4
- Letter Spacing: 0.02em
- Color: Dark gray
- Use: Card titles, list headers, minor sections

### Body Text

**Body Copy (Paragraph Text)**
- Font: Inter Regular (400)
- Size: 16px (desktop), 14-15px (mobile)
- Line Height: 1.6
- Letter Spacing: 0em
- Color: #111111 (dark gray-black)
- Paragraph Spacing: 16px bottom margin
- Use: Main content paragraphs, documentation

**Small Text / Caption**
- Font: Inter Regular (400)
- Size: 12-14px
- Line Height: 1.5
- Letter Spacing: 0.01em
- Color: #666666 (medium gray)
- Use: Figure captions, footnotes, helper text

**Emphasis Text (Bold)**
- Font: Inter SemiBold (600)
- Use: Important words, emphasis points
- Color: Maintain color of surrounding text

### UI Elements

**Button Text**
- Font: Poppins SemiBold (600)
- Size: 14-16px
- Letter Spacing: 0.05em
- Case: Sentence case (capitalize first word)
- Use: "Enroll Now", "Learn More", etc.

**Navigation Text**
- Font: Inter SemiBold (600)
- Size: 14-16px
- Letter Spacing: 0.02em
- Case: Sentence case or Title Case
- Use: Menu items, breadcrumbs, links

**Form Labels**
- Font: Inter SemiBold (600)
- Size: 14px
- Letter Spacing: 0.01em
- Color: #111111
- Use: Form field labels, required indicators

---

## 🎨 FONT PAIRING MATRIX

**Tested Pairings:**

| Heading | Body | Notes | Rating |
|---------|------|-------|--------|
| **Poppins 800** | Inter 400 | Geometric + Humanist (RECOMMENDED) | ⭐⭐⭐⭐⭐ |
| Poppins 700 | Lato 400 | Geometric + Warm (friendly feel) | ⭐⭐⭐⭐ |
| Raleway 700 | Inter 400 | Elegant + Clean (premium feel) | ⭐⭐⭐⭐ |
| Inter 700 | Inter 400 | Single-family (cohesive, simple) | ⭐⭐⭐⭐ |
| Work Sans 700 | Source Sans Pro 400 | Technical + Professional | ⭐⭐⭐⭐ |

**Recommendation: Poppins + Inter**
- Maximum contrast in personality (visual interest)
- Excellent readability
- Modern and professional
- Completely free and open-source
- Pairs perfectly with geometric logo aesthetics

---

## 💻 CSS IMPLEMENTATION

### Web Fonts (Google Fonts)

```css
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap');

/* Root variables */
:root {
  /* Display font */
  --font-display: 'Poppins', sans-serif;
  --font-display-weight: 700;
  
  /* Body font */
  --font-body: 'Inter', sans-serif;
  --font-body-weight: 400;
  --font-body-weight-semibold: 600;
  
  /* Font sizes */
  --fs-h1: 3rem;        /* 48px */
  --fs-h2: 2rem;        /* 32px */
  --fs-h3: 1.5rem;      /* 24px */
  --fs-body: 1rem;      /* 16px */
  --fs-small: 0.875rem; /* 14px */
  
  /* Line heights */
  --lh-display: 1.2;
  --lh-heading: 1.4;
  --lh-body: 1.6;
}

/* Heading styles */
h1 {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: var(--fs-h1);
  line-height: var(--lh-display);
  letter-spacing: -0.02em;
  color: #0066CC; /* Primary brand color */
}

h2 {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: var(--fs-h2);
  line-height: var(--lh-heading);
  color: #111111;
}

h3 {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: var(--fs-h3);
  line-height: var(--lh-heading);
  color: #333333;
}

/* Body text */
body {
  font-family: var(--font-body);
  font-weight: var(--font-body-weight);
  font-size: var(--fs-body);
  line-height: var(--lh-body);
  color: #111111;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  :root {
    --fs-h1: 2rem;
    --fs-h2: 1.5rem;
    --fs-h3: 1.25rem;
    --fs-body: 0.95rem;
  }
}
```

### Font Loading Performance

**Font strategy:** System fonts + web fonts (critical path optimized)

```html
<!-- Critical font (display) -->
<link rel="preload" as="font" href="/fonts/poppins-700.woff2" type="font/woff2" crossorigin>
<link rel="preload" as="font" href="/fonts/poppins-800.woff2" type="font/woff2" crossorigin>

<!-- Non-critical fonts (defer) -->
<link rel="preload" as="font" href="/fonts/inter-400.woff2" type="font/woff2" crossorigin>

<!-- Fallback system fonts (FOUT strategy) -->
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif; }
</style>

<!-- Web fonts (with font-display: swap) -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## 🖨️ PRINT SPECIFICATIONS

### Print Font Files Needed

1. **Poppins** (heading font)
   - File: Poppins-Bold.ttf or .otf
   - Weights: 600, 700, 800
   - Format: OpenType (OTF or TTF)

2. **Inter** (body font)
   - File: Inter-Regular.ttf and Inter-SemiBold.ttf
   - Weights: 400, 600
   - Format: OpenType (OTF or TTF)

3. **Font Licenses**
   - Both fonts: Open Font License (OFL) - free for commercial use
   - No embedding restrictions
   - Can be included in printed materials

### Print Font Sizing

**Business Card (2" x 3.5")**
- Heading: 12-14pt
- Body: 8-10pt

**Website Body Text (72 DPI screen)**
- 16px = ~12pt print equivalent
- Maintains readability across media

---

## 📋 TYPOGRAPHY CHECKLIST

**By Feb 3, Confirm:**

- [ ] Font family decisions locked in (Poppins + Inter)
- [ ] CSS variables defined and tested
- [ ] Google Fonts setup confirmed
- [ ] Font loading performance tested
- [ ] Print specs documented
- [ ] Fallback fonts defined
- [ ] Web rendering tested on multiple browsers
- [ ] Mobile typography tested
- [ ] Dark mode typography (if applicable)
- [ ] Accessibility standards met (WCAG AA)
- [ ] Font pairing mockups created
- [ ] Documentation complete

---

## 📊 FINAL TYPOGRAPHY SYSTEM

**Selected System:**

| Element | Font | Weight | Size | Color |
|---------|------|--------|------|-------|
| Logo Text | Poppins | 800 | 48-64px | Primary Blue |
| H1 Headlines | Poppins | 800 | 48px | Primary Blue |
| H2 Headings | Poppins | 700 | 32px | Black |
| H3 Subheadings | Poppins | 600 | 24px | Dark Gray |
| Body Text | Inter | 400 | 16px | Dark Gray |
| Emphasis | Inter | 600 | 16px | Black |
| Captions | Inter | 400 | 12px | Medium Gray |
| UI/Buttons | Poppins | 600 | 14-16px | Varies |

---

## 🚀 NEXT STEPS

1. **@CTO:** Implement CSS variables and web fonts
2. **@Admin:** Document typography in brand guidelines
3. **Team:** Test typography with logo concepts (Feb 2)
4. **QA:** Verify rendering across browsers/devices (Feb 3)

---

**Status:** 🟢 READY FOR IMPLEMENTATION

*Typography system is finalized and ready for web and print integration. Both fonts are free, open-source, and fully accessible.*

Questions? Contact @CTO for technical specifications.
