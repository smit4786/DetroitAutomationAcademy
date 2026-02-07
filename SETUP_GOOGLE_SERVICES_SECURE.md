# 🔒 INTERNAL ONLY - DO NOT DISTRIBUTE PUBLICLY
**Confidential - Detroit Automation Academy**

This document contains sensitive setup procedures and configuration details.
Distribution is restricted to authorized team members only.
Do NOT share outside the organization or commit unredacted to public repositories.

---

# Google Services Secure Setup Guide
**Detroit Automation Academy - Internal Documentation**

**Version:** 2.0 (Security-First Rebuild)  
**Last Updated:** February 2026  
**Classification:** INTERNAL ONLY

---

## 🎯 OVERVIEW

This guide provides step-by-step instructions for securely configuring Google Calendar integration for Detroit Automation Academy. All sensitive credentials are managed through environment variables and NEVER hardcoded in scripts or public documentation.

---

## 📋 PREREQUISITES

### Required Access
- [ ] Google account with Calendar access ([INTERNAL - See team password manager])
- [ ] Access to Google Cloud Console
- [ ] Git repository access
- [ ] Local development environment

### Required Tools
- [ ] Python 3.8+ installed
- [ ] pip package manager
- [ ] Git command line tools
- [ ] Text editor (VS Code recommended)

---

## 🔐 PART 1: GOOGLE CLOUD SETUP

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Sign in with organization Google account: **[INTERNAL - See .env file]**
3. Click "Select a project" → "New Project"
4. Enter project details:
   - **Project Name:** Detroit Automation Academy
   - **Organization:** [INTERNAL]
   - **Location:** No organization
5. Click "Create"
6. Wait for project creation (1-2 minutes)

### Step 2: Enable Google Calendar API

1. In Google Cloud Console, select your project
2. Navigate to **APIs & Services** → **Library**
3. Search for "Google Calendar API"
4. Click on "Google Calendar API"
5. Click "Enable"
6. Wait for API activation (30 seconds)

### Step 3: Create OAuth 2.0 Credentials

**For Desktop Application (Interactive):**

1. Navigate to **APIs & Services** → **Credentials**
2. Click "Create Credentials" → "OAuth client ID"
3. Configure OAuth consent screen (if first time):
   - User Type: **Internal** (if available) or **External**
   - App name: **Detroit Automation Academy Calendar**
   - User support email: **[INTERNAL - See .env]**
   - Developer contact: **[INTERNAL - See .env]**
   - Click "Save and Continue"
4. Scopes: Add `https://www.googleapis.com/auth/calendar`
5. Test users: Add your Google account email
6. Click "Save and Continue"
7. Return to **Credentials** → "Create Credentials" → "OAuth client ID"
8. Application type: **Desktop app**
9. Name: **DAA Calendar Desktop Client**
10. Click "Create"
11. Download credentials:
    - Click "Download JSON"
    - Save as `credentials.json`
    - **IMPORTANT:** This file contains sensitive data

**For Service Account (Automated):**

1. Navigate to **APIs & Services** → **Credentials**
2. Click "Create Credentials" → "Service account"
3. Service account details:
   - Name: **DAA Calendar Service**
   - ID: `daa-calendar-service`
   - Description: **Automated calendar management**
4. Click "Create and Continue"
5. Grant role: **Project → Editor** (or Calendar-specific role)
6. Click "Continue" → "Done"
7. Click on the created service account
8. Go to "Keys" tab
9. Click "Add Key" → "Create new key"
10. Key type: **JSON**
11. Click "Create"
12. Download key file → Save as `credentials.json`

⚠️ **SECURITY NOTE:** The credentials file contains sensitive authentication data. Treat it like a password.

---

## 🔧 PART 2: LOCAL ENVIRONMENT SETUP

### Step 1: Clone Repository (if not already done)

```bash
cd ~/Documents/gitHub
git clone https://github.com/[INTERNAL]/DetroitAutomationAcademy.git
cd DetroitAutomationAcademy
```

### Step 2: Verify .gitignore Protection

```bash
# Verify .env and credentials are protected
git check-ignore -v .env
git check-ignore -v credentials.json
git check-ignore -v token.pickle

# Should show:
# .gitignore:105:.env    .env
# [Similar for credentials.json and token.pickle]
```

If not protected, add to `.gitignore`:
```bash
echo "credentials.json" >> .gitignore
echo "token.pickle" >> .gitignore
```

### Step 3: Install Python Dependencies

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows

# Install required packages
pip install --upgrade pip
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
pip install icalendar python-dateutil python-dotenv

# Save requirements
pip freeze > requirements.txt
```

### Step 4: Place Credentials File

```bash
# Move downloaded credentials.json to project root
mv ~/Downloads/credentials.json .

# Set secure permissions (read/write for owner only)
chmod 600 credentials.json

# Verify it's gitignored
git status | grep credentials.json
# Should show: nothing (file is ignored)
```

⚠️ **CRITICAL:** NEVER commit `credentials.json` to git

---

## 🔑 PART 3: CONFIGURE ENVIRONMENT VARIABLES

### Step 1: Create .env File from Template

```bash
# Copy template
cp .env.example .env

# Set secure permissions
chmod 600 .env

# Verify it's gitignored
git status | grep .env
# Should show: nothing (file is ignored)
```

### Step 2: Configure Environment Variables

Open `.env` in your text editor and set the following values:

```bash
# =============================================================================
# GOOGLE CALENDAR API CREDENTIALS
# =============================================================================
# Account email - [INTERNAL USE ONLY]
GOOGLE_ACCOUNT_EMAIL=[INTERNAL - Contact team lead for value]

# Calendar ID (usually same as account email for primary calendar)
GOOGLE_CALENDAR_ID=[INTERNAL - Contact team lead for value]

# Path to credentials file
GOOGLE_API_CREDENTIALS_FILE=credentials.json

# Token storage file (auto-generated)
GOOGLE_TOKEN_FILE=token.pickle

# =============================================================================
# GITHUB INTEGRATION
# =============================================================================
GITHUB_TOKEN=[INTERNAL - Generate at https://github.com/settings/tokens]
GITHUB_REPO_OWNER=[INTERNAL - Repository owner]
GITHUB_REPO_NAME=DetroitAutomationAcademy

# =============================================================================
# OPERATIONAL SETTINGS
# =============================================================================
APP_ENV=development
TZ=America/Detroit
```

### Step 3: Validate Environment Configuration

Run the validation script:

```bash
python3 scripts/validate_env.py
```

Expected output:
```
🔍 Validating environment variables...
✅ Found: GOOGLE_ACCOUNT_EMAIL
✅ Found: GOOGLE_CALENDAR_ID
✅ Found: GOOGLE_API_CREDENTIALS_FILE

✅ All required environment variables are set
```

---

## 🧪 PART 4: TEST GOOGLE CALENDAR CONNECTION

### Step 1: Run Setup Script

```bash
./setup_google_calendar_secure.sh
```

This script will:
1. Check for required files
2. Validate environment variables
3. Test Google Calendar API connection
4. Create test event (optional)
5. Verify authentication

### Step 2: Manual Authentication Test

```python
# Run Python interactively
python3

>>> from dotenv import load_dotenv
>>> load_dotenv()
True
>>> import os
>>> # Verify variables loaded (DON'T print actual values)
>>> bool(os.getenv('GOOGLE_ACCOUNT_EMAIL'))
True
>>> bool(os.getenv('GOOGLE_CALENDAR_ID'))
True
>>> exit()
```

### Step 3: Test Calendar Import

```bash
# Test with sample calendar file
python3 import_calendar_to_google.py \
    --calendar-file BGC_EVENT_READY_CALENDAR.ics \
    --calendar-name "Detroit Automation Academy"
```

Expected output:
```
🚀 Detroit Automation Academy - Google Calendar Importer
============================================================
📋 Calendar file: BGC_EVENT_READY_CALENDAR.ics
📅 Target calendar: Detroit Automation Academy
============================================================

🔐 Authenticating with Google Calendar API...
✅ Authenticated with Google account

📅 Setting up calendar: Detroit Automation Academy
✅ Found calendar: Detroit Automation Academy (ID: [REDACTED])

📥 Importing events from BGC_EVENT_READY_CALENDAR.ics...
📋 Found 1 events in ICS file
✅ Imported: Boys & Girls Club Event - Day 2
   Time: 2026-02-04 07:30:00 → 2026-02-04 14:00:00
   Attendees: 2

============================================================
✅ SUCCESS: 1 event(s) imported to Google Calendar
📅 Calendar: Detroit Automation Academy
🔗 View at: https://calendar.google.com
```

---

## 🚨 TROUBLESHOOTING

### Issue: "credentials.json not found"

**Solution:**
1. Verify credentials.json is in project root: `ls -la credentials.json`
2. If missing, download again from Google Cloud Console
3. Check file permissions: `chmod 600 credentials.json`

### Issue: "GOOGLE_ACCOUNT_EMAIL not set"

**Solution:**
1. Verify .env file exists: `ls -la .env`
2. Check .env content: `cat .env | grep GOOGLE_ACCOUNT_EMAIL`
3. Ensure no spaces around `=` in .env: `GOOGLE_ACCOUNT_EMAIL=value` (not `GOOGLE_ACCOUNT_EMAIL = value`)
4. Load environment in script: `from dotenv import load_dotenv; load_dotenv()`

### Issue: "API not enabled"

**Solution:**
1. Go to Google Cloud Console
2. Select project
3. Navigate to **APIs & Services** → **Library**
4. Search "Google Calendar API"
5. Click "Enable"

### Issue: "Insufficient permissions"

**Solution:**
1. Check OAuth scopes include: `https://www.googleapis.com/auth/calendar`
2. For service account: Grant "Calendar Editor" role
3. Delete `token.pickle` and re-authenticate
4. Ensure calendar is shared with service account email (for service accounts)

### Issue: "Invalid credentials"

**Solution:**
1. Verify credentials.json is valid JSON: `python3 -m json.tool credentials.json`
2. Check credentials weren't modified or corrupted
3. Re-download from Google Cloud Console if needed
4. Ensure using correct credential type (OAuth vs Service Account)

---

## 🔄 PART 5: TEAM CREDENTIAL SHARING

### For New Team Members

**DO NOT share credentials via:**
- ❌ Email
- ❌ Slack/Teams
- ❌ Text message
- ❌ Public documentation
- ❌ Git commits

**ACCEPTABLE methods:**
- ✅ Secure password manager (1Password, LastPass, Bitwarden)
- ✅ Encrypted file transfer (GPG encrypted)
- ✅ In-person handoff
- ✅ Secure internal wiki (with access controls)

### Onboarding Procedure

1. **Team Lead:** Share credentials via secure password manager
2. **New Member:** 
   - Clone repository
   - Create `.env` from template
   - Copy credentials from password manager to `.env`
   - Place `credentials.json` in project root
   - Run validation: `python3 scripts/validate_env.py`
   - Test connection: `./setup_google_calendar_secure.sh`
3. **Verify:** Ensure `.env` and `credentials.json` are NOT tracked by git

---

## 🔐 SECURITY BEST PRACTICES

### Credential Rotation

**Schedule:**
- Rotate Google API credentials: Every 90 days
- Rotate GitHub tokens: Every 90 days
- Review access permissions: Monthly

**Procedure:**
1. Generate new credentials in Google Cloud Console
2. Download new `credentials.json`
3. Replace old file
4. Delete `token.pickle` to force re-authentication
5. Test connection
6. Revoke old credentials in console
7. Update team password manager

### Access Control

**Who has access:**
- Google Account: [INTERNAL - Team lead, admins only]
- Google Cloud Console: [INTERNAL - Technical team only]
- .env file: Each developer (local copy only)
- credentials.json: Each developer (local copy only)

**Audit regularly:**
```bash
# Check what files are NOT gitignored
git ls-files | grep -E '(\.env|credentials\.json|token\.pickle)'
# Should return: nothing

# Check for exposed credentials in git history
git log --all --full-history --source --raw -- '*credentials*' '*.env'
# Should return: nothing sensitive
```

### File Permissions

```bash
# Set restrictive permissions on sensitive files
chmod 600 .env
chmod 600 credentials.json
chmod 600 token.pickle  # if exists

# Verify
ls -la | grep -E '(\.env|credentials\.json|token\.pickle)'
# Should show: -rw------- (read/write for owner only)
```

---

## 📚 ADDITIONAL RESOURCES

### Internal Documentation
- `AGENT_SECURITY_PROCEDURES.md` - Security rules for AI agents
- `SECURITY_PROCEDURES.md` - General security guidelines
- `.env.example` - Environment variable template (safe for git)
- `SECURITY_BREACH_LOG.md` - Incident tracking (if applicable)

### External Resources
- [Google Calendar API Documentation](https://developers.google.com/calendar/api/guides/overview)
- [OAuth 2.0 Best Practices](https://oauth.net/2/best-practices/)
- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

### Support Contacts
- **Technical Issues:** CTO Office
- **Access Issues:** Team Lead / Administrator
- **Security Concerns:** Escalate immediately to CTO

---

## ✅ SETUP VERIFICATION CHECKLIST

**Before using Google Calendar integration:**

- [ ] Google Cloud Project created
- [ ] Google Calendar API enabled
- [ ] OAuth credentials created and downloaded
- [ ] `credentials.json` placed in project root (chmod 600)
- [ ] `.env` file created from `.env.example`
- [ ] All environment variables configured in `.env`
- [ ] `.env` and `credentials.json` are in `.gitignore`
- [ ] Python dependencies installed
- [ ] Validation script passes: `python3 scripts/validate_env.py`
- [ ] Test connection successful: `./setup_google_calendar_secure.sh`
- [ ] Can import calendar event successfully
- [ ] No sensitive data committed to git: `git status`

---

## 🔄 MAINTENANCE

### Monthly Tasks
- [ ] Review access permissions
- [ ] Audit git history for exposed credentials
- [ ] Verify `.gitignore` is up to date
- [ ] Check for deprecated API versions
- [ ] Update dependencies: `pip install --upgrade -r requirements.txt`

### Quarterly Tasks
- [ ] Rotate Google API credentials
- [ ] Rotate GitHub tokens
- [ ] Review and update security procedures
- [ ] Audit API usage in Google Cloud Console
- [ ] Clean up old tokens and credentials

---

**Document Version:** 2.0 (Security Rebuild)  
**Created:** February 2026  
**Last Updated:** February 2026  
**Next Review:** March 2026  
**Owner:** CTO Office, Automated Technologies

**Classification:** 🔒 INTERNAL ONLY  
**Distribution:** Authorized team members only  
**Do NOT commit unredacted to public repository**

---

*For questions or issues, contact the CTO office. Security is our top priority.*
