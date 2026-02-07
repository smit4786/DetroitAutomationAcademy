#!/bin/bash
# =============================================================================
# SECURE GOOGLE CALENDAR SETUP SCRIPT
# Detroit Automation Academy
# =============================================================================
# SECURITY: This script prompts for sensitive configuration at runtime.
# No credentials are hardcoded. All values are saved to .env (gitignored).
# =============================================================================

set -e  # Exit on error

echo "🔐 Detroit Automation Academy - Secure Google Calendar Setup"
echo "============================================================="
echo ""
echo "This script will securely configure Google Calendar integration."
echo "All sensitive data will be stored in .env (NOT committed to git)."
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# =============================================================================
# STEP 1: VERIFY ENVIRONMENT
# =============================================================================

echo "📋 Step 1: Verifying environment..."
echo ""

# Check if .gitignore exists and protects .env
if [ ! -f ".gitignore" ]; then
    echo -e "${RED}❌ ERROR: .gitignore not found${NC}"
    exit 1
fi

if ! grep -q "^\.env$" .gitignore; then
    echo -e "${YELLOW}⚠️  .env not in .gitignore - adding now${NC}"
    echo "" >> .gitignore
    echo "# Environment variables (sensitive)" >> .gitignore
    echo ".env" >> .gitignore
    echo -e "${GREEN}✅ Added .env to .gitignore${NC}"
else
    echo -e "${GREEN}✅ .env is protected by .gitignore${NC}"
fi

# Check if credentials.json is protected
if ! grep -q "credentials\.json" .gitignore; then
    echo -e "${YELLOW}⚠️  credentials.json not in .gitignore - adding now${NC}"
    echo "credentials.json" >> .gitignore
    echo "token.pickle" >> .gitignore
    echo -e "${GREEN}✅ Added credentials.json to .gitignore${NC}"
else
    echo -e "${GREEN}✅ credentials.json is protected by .gitignore${NC}"
fi

echo ""

# =============================================================================
# STEP 2: CHECK FOR EXISTING .env
# =============================================================================

echo "📋 Step 2: Checking for existing .env file..."
echo ""

if [ -f ".env" ]; then
    echo -e "${YELLOW}⚠️  Existing .env file found${NC}"
    echo ""
    read -p "Do you want to overwrite it? (y/N): " overwrite
    if [ "$overwrite" != "y" ] && [ "$overwrite" != "Y" ]; then
        echo ""
        echo "Setup cancelled. Your existing .env file was not modified."
        echo "To manually edit: nano .env"
        exit 0
    fi
    echo ""
fi

# =============================================================================
# STEP 3: VERIFY .env.example EXISTS
# =============================================================================

echo "📋 Step 3: Verifying .env.example template..."
echo ""

if [ ! -f ".env.example" ]; then
    echo -e "${RED}❌ ERROR: .env.example template not found${NC}"
    echo ""
    echo "The .env.example file should exist in the repository."
    echo "It contains the template for environment variables."
    exit 1
fi

echo -e "${GREEN}✅ .env.example template found${NC}"
echo ""

# =============================================================================
# STEP 4: PROMPT FOR CREDENTIALS (SECURE INPUT)
# =============================================================================

echo "📋 Step 4: Configure Google Calendar credentials..."
echo ""
echo -e "${YELLOW}⚠️  SECURITY NOTE:${NC}"
echo "Your inputs will be saved to .env (local only, NOT committed to git)"
echo "Press Ctrl+C at any time to cancel"
echo ""

# Prompt for Google Account Email
while true; do
    read -p "Enter Google Account Email: " google_email
    if [[ "$google_email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        break
    else
        echo -e "${RED}❌ Invalid email format. Please try again.${NC}"
    fi
done

# Prompt for Google Calendar ID (default to email)
echo ""
echo "Google Calendar ID (press Enter to use same as account email):"
read -p "Calendar ID [default: $google_email]: " google_calendar_id
if [ -z "$google_calendar_id" ]; then
    google_calendar_id="$google_email"
fi

# Check for credentials.json
echo ""
echo "📋 Checking for Google API credentials file..."
if [ ! -f "credentials.json" ]; then
    echo -e "${YELLOW}⚠️  credentials.json not found${NC}"
    echo ""
    echo "Please download credentials.json from Google Cloud Console:"
    echo "1. Go to https://console.cloud.google.com/apis/credentials"
    echo "2. Create OAuth 2.0 Client ID (Desktop app)"
    echo "3. Download JSON file"
    echo "4. Save as 'credentials.json' in this directory"
    echo ""
    read -p "Press Enter once you've placed credentials.json in this directory..."
    
    if [ ! -f "credentials.json" ]; then
        echo -e "${RED}❌ ERROR: credentials.json still not found${NC}"
        echo "Setup cannot continue without credentials file"
        exit 1
    fi
fi

echo -e "${GREEN}✅ credentials.json found${NC}"

# Set secure permissions on credentials.json
chmod 600 credentials.json 2>/dev/null || echo -e "${YELLOW}⚠️  Could not set permissions on credentials.json${NC}"

# =============================================================================
# STEP 5: CREATE .env FILE
# =============================================================================

echo ""
echo "📋 Step 5: Creating .env file..."
echo ""

cat > .env << EOF
# =============================================================================
# DETROIT AUTOMATION ACADEMY - ENVIRONMENT VARIABLES
# =============================================================================
# ⚠️  SECURITY WARNING: DO NOT COMMIT THIS FILE TO GIT
# This file is automatically generated by setup_google_calendar_secure.sh
# Last updated: $(date)
# =============================================================================

# -----------------------------------------------------------------------------
# GOOGLE CALENDAR API CREDENTIALS
# -----------------------------------------------------------------------------
# Google account email used for calendar operations
GOOGLE_ACCOUNT_EMAIL=${google_email}

# Google Calendar ID (usually same as account email or custom calendar ID)
GOOGLE_CALENDAR_ID=${google_calendar_id}

# Path to Google API credentials JSON file
GOOGLE_API_CREDENTIALS_FILE=credentials.json

# Path to stored OAuth token (generated automatically on first run)
GOOGLE_TOKEN_FILE=token.pickle

# -----------------------------------------------------------------------------
# OPERATIONAL SETTINGS
# -----------------------------------------------------------------------------
# Application environment
APP_ENV=development

# Timezone for calendar operations
TZ=America/Detroit

# =============================================================================
# SECURITY REMINDERS
# =============================================================================
# ✅ This file is in .gitignore and will NOT be committed
# ✅ NEVER share this file or commit to version control
# ✅ For team setup, see: SETUP_GOOGLE_SERVICES_SECURE.md
# =============================================================================
EOF

# Set secure permissions on .env
chmod 600 .env

echo -e "${GREEN}✅ .env file created with secure permissions (600)${NC}"
echo ""

# =============================================================================
# STEP 6: VALIDATE CONFIGURATION
# =============================================================================

echo "📋 Step 6: Validating configuration..."
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}⚠️  Python 3 not found - skipping validation${NC}"
    echo "Please manually verify your setup"
else
    # Check if required Python packages are installed
    if ! python3 -c "import dotenv" 2>/dev/null; then
        echo -e "${YELLOW}⚠️  python-dotenv not installed${NC}"
        echo "Installing required Python packages..."
        pip3 install python-dotenv google-auth-oauthlib google-auth-httplib2 google-api-python-client icalendar python-dateutil
    fi
    
    # Validate environment variables
    python3 << 'PYEOF'
import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 Validating environment variables...")
print("")

required_vars = [
    "GOOGLE_ACCOUNT_EMAIL",
    "GOOGLE_CALENDAR_ID",
    "GOOGLE_API_CREDENTIALS_FILE",
]

all_set = True
for var in required_vars:
    value = os.getenv(var)
    if value:
        # Show that variable is set without exposing the value
        if '@' in value:
            # Email - show redacted
            parts = value.split('@')
            masked = f"{parts[0][:2]}***@{parts[1]}"
            print(f"✅ {var}: {masked}")
        else:
            # Other values
            print(f"✅ {var}: [SET]")
    else:
        print(f"❌ {var}: [NOT SET]")
        all_set = False

print("")

if all_set:
    print("✅ All required environment variables are configured")
    exit(0)
else:
    print("❌ Some required variables are missing")
    exit(1)
PYEOF

    validation_result=$?
    
    if [ $validation_result -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Configuration validation passed${NC}"
    else
        echo ""
        echo -e "${RED}❌ Configuration validation failed${NC}"
        echo "Please check your .env file and try again"
        exit 1
    fi
fi

echo ""

# =============================================================================
# STEP 7: TEST CONNECTION (OPTIONAL)
# =============================================================================

echo "📋 Step 7: Test Google Calendar connection..."
echo ""
echo "Would you like to test the Google Calendar API connection now?"
echo "(This will open a browser window for OAuth authentication)"
echo ""
read -p "Test connection? (y/N): " test_connection

if [ "$test_connection" = "y" ] || [ "$test_connection" = "Y" ]; then
    echo ""
    echo "🔐 Testing Google Calendar API connection..."
    echo "A browser window will open for authentication..."
    echo ""
    
    python3 << 'PYEOF'
import os
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    import pickle
except ImportError:
    print("❌ Required Python packages not installed")
    print("Run: pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def test_connection():
    """Test Google Calendar API connection"""
    creds = None
    token_file = os.getenv('GOOGLE_TOKEN_FILE', 'token.pickle')
    creds_file = os.getenv('GOOGLE_API_CREDENTIALS_FILE', 'credentials.json')
    
    # Check for existing token
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_file):
                print(f"❌ Credentials file not found: {creds_file}")
                return False
            
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
        
        # Set secure permissions
        os.chmod(token_file, 0o600)
    
    # Test API call
    try:
        service = build('calendar', 'v3', credentials=creds)
        
        # List calendars
        calendar_list = service.calendarList().list(maxResults=10).execute()
        calendars = calendar_list.get('items', [])
        
        print("✅ Successfully connected to Google Calendar API")
        print("")
        print(f"📅 Found {len(calendars)} calendar(s):")
        for cal in calendars[:5]:  # Show first 5
            print(f"   • {cal['summary']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        return False

if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1)
PYEOF

    test_result=$?
    
    if [ $test_result -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Google Calendar connection test PASSED${NC}"
    else
        echo ""
        echo -e "${YELLOW}⚠️  Connection test failed${NC}"
        echo "This might be normal on first setup. Try running import_calendar_to_google.py"
    fi
fi

# =============================================================================
# COMPLETION
# =============================================================================

echo ""
echo "============================================================="
echo -e "${GREEN}✅ SETUP COMPLETE!${NC}"
echo "============================================================="
echo ""
echo "📋 Summary:"
echo "   • .env file created with secure permissions"
echo "   • credentials.json verified"
echo "   • Environment variables configured"
echo "   • Files protected by .gitignore"
echo ""
echo "🎯 Next Steps:"
echo ""
echo "1. Import a calendar event:"
echo "   python3 import_calendar_to_google.py --calendar-file YOUR_FILE.ics"
echo ""
echo "2. View secure setup documentation:"
echo "   cat SETUP_GOOGLE_SERVICES_SECURE.md"
echo ""
echo "3. Review security procedures:"
echo "   cat AGENT_SECURITY_PROCEDURES.md"
echo ""
echo "⚠️  SECURITY REMINDERS:"
echo "   • NEVER commit .env or credentials.json to git"
echo "   • NEVER share these files via email or Slack"
echo "   • DO rotate credentials every 90 days"
echo "   • DO use secure password manager for team sharing"
echo ""
echo "📞 Questions? See SETUP_GOOGLE_SERVICES_SECURE.md (INTERNAL ONLY)"
echo "============================================================="
