# 🚀 Deployment Guide - GitHub Pages Website

**Status:** Website deployment infrastructure setup  
**Last Updated:** February 9, 2026  
**Current Issue:** Email privacy blocker on git push

---

## ⚠️ IMMEDIATE ACTION REQUIRED

Your commit `e56eebf` contains the personal email address `jsmith34@ccsdetroit.edu`, which GitHub's privacy protection is blocking. Follow these steps to resolve:

### Step 1: Configure Git with Noreply Email

```bash
git config --global user.email "smit4786@users.noreply.github.com"
git config --global user.name "JustinSmith"
```

**Verify:**
```bash
git config --global user.email
```

Should output: `smit4786@users.noreply.github.com`

---

### Step 2: Amend the Unpushed Commit

```bash
git commit --amend --no-edit
```

This will rewrite the commit metadata with the noreply email without changing the code.

---

### Step 3: Force Push to GitHub

```bash
git push --force-with-lease
```

**Expected output:**
```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using 100% (4/4), done.
Writing objects: 100% (4/4), 518 bytes | 518.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/smit4786/DetroitAutomationAcademy.git
   [forced update]
   main -> main
```

---

### Step 4: Verify GitHub Pages Deployment

Once the push succeeds:

1. **Wait 1-2 minutes** for GitHub Pages to rebuild.
2. **Visit the GitHub Pages URL (works immediately):**
   ```
   https://smit4786.github.io/DetroitAutomationAcademy/docs/BGC_EVENT_STATUS_DASHBOARD.html
   ```
3. **Or use the custom domain (after DNS setup):**
   ```
   https://detroitautomationacademy.com/docs/BGC_EVENT_STATUS_DASHBOARD.html
   ```
4. **Confirm the dashboard renders** with all tiles visible.

---

## 🌐 Custom Domain Setup (detroitautomationacademy.com)

The repository has a CNAME file configured, but the custom domain requires DNS configuration at your registrar.

### Step 1: Get Your Domain Registrar Login
Log into your domain registrar (GoDaddy, Namecheap, Google Domains, etc.) where `detroitautomationacademy.com` is registered.

### Step 2: Add DNS A Records

Add **all four** of these DNS A records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

**Notes:**
- `@` means the root domain (detroitautomationacademy.com)
- All four IP addresses are required for GitHub Pages
- Remove any existing A records for the root domain

### Step 3: (Optional) Add CNAME for www

For www subdomain support, add:

| Type | Name | Value |
|------|------|-------|
| CNAME | www | smit4786.github.io |

### Step 4: Verify GitHub Pages Settings

1. Go to: https://github.com/smit4786/DetroitAutomationAcademy/settings/pages
2. Under "Custom domain", verify it shows: `detroitautomationacademy.com`
3. Ensure "Enforce HTTPS" is **checked**

### Step 5: Wait for DNS Propagation

DNS changes take **24-48 hours** to fully propagate. During this time:
- Use GitHub Pages URL: `https://smit4786.github.io/DetroitAutomationAcademy/...`
- Check propagation: https://www.whatsmydns.net/?domain=detroitautomationacademy.com

### Step 6: Verify Custom Domain Works

After 24-48 hours, test:
```
https://detroitautomationacademy.com/docs/BGC_EVENT_STATUS_DASHBOARD.html
```

Should load without 404 error.

---

## 🔧 Ongoing Deployment Workflow

### Manual Workflow (Current)
1. Make changes to files in `docs/`
2. Commit with new noreply email config: `git commit -m "Update dashboard"`
3. Push: `git push`
4. Wait 1-2 minutes for GitHub Pages rebuild

### Automated Workflow (Recommended)
See `.github/workflows/deploy-pages.yml` for CI/CD automation (coming in next step).

---

## 📁 Website Structure for GitHub Pages

```
docs/
├── BGC_EVENT_STATUS_DASHBOARD.html    ← Main public dashboard
├── INDEX.md                           ← Navigation hub
├── quick_start.md
├── phase1_guide.md
├── phase2_guide.md
├── phase3_guide.md
├── api_reference.md
├── bgc_event_guide.md
├── token_design_concepts.md
└── PROJECT_PLAN.md
```

**All files in `docs/` are publicly accessible via GitHub Pages.**

---

## 🛡️ Privacy & Security Checklist

Before publishing any file:

- [ ] **No personal emails** in commit history (use noreply)
- [ ] **No API keys/tokens** in code or documentation
- [ ] **No sensitive data** (addresses, phone numbers, passwords)
- [ ] **Anonymize examples** (use placeholder names/emails)
- [ ] **Review metadata** (git author, file properties)

**Reference:** ADMINISTRATIVE_COORDINATION_PLAN.md (Privacy Workflow section)

---

## 🚀 Next Steps

1. **Execute the 4 steps above** to push the current commit
2. **Verify the dashboard is live** at the public URL
3. **Enable GitHub Actions** (optional) for automated future deployments
4. **Document any custom setup** in this guide

---

## 📊 Deployment Status

| Component | Status | Details |
|-----------|--------|---------|
| GitHub Pages Enabled | ✅ | main branch, docs/ folder |
| Dashboard File | ⏳ | In `docs/`, awaiting push |
| Email Configuration | 🔄 | Run git config commands above |
| Push Status | ❌ | Blocked by email privacy |
| Public URL | 📅 | Will be live after push succeeds |

---

## 🆘 Troubleshooting

### Push Still Fails After Git Config
```bash
# Check current git config
git config --global user.email

# If still showing old email, reset and retry
git config --global --unset user.email
git config --global user.email "smit4786@users.noreply.github.com"
git commit --amend --no-edit
git push --force-with-lease
```

### Dashboard Not Appearing After Push
1. Wait 2-3 minutes for GitHub Pages rebuild
2. Check GitHub Actions tab: Settings > Pages > Build logs
3. Verify file exists: https://github.com/smit4786/DetroitAutomationAcademy/blob/main/docs/BGC_EVENT_STATUS_DASHBOARD.html
4. Clear browser cache and retry

### Branch Protection Issues
If your repository has branch protection enabled:
```bash
# Use regular push instead of force
git push
```

---

## 📚 Related Documentation

- [MASTER_DOCUMENT_INDEX.md](MASTER_DOCUMENT_INDEX.md) - Complete documentation navigation
- [ADMINISTRATIVE_COORDINATION_PLAN.md](ADMINISTRATIVE_COORDINATION_PLAN.md) - Privacy & stakeholder coordination
- [README.md](README.md) - Project overview

---

**Prepared by:** Development & Infrastructure Team  
**Distribution:** All Developers, Admin Staff  
**Audience:** Technical Staff, DevOps, Leadership

