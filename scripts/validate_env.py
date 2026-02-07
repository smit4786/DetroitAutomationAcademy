#!/usr/bin/env python3
"""
Environment Variable Validation Script
Detroit Automation Academy

SECURITY: Validates that required environment variables are set
without exposing actual values.

Usage:
    python3 scripts/validate_env.py
"""

import os
import sys
from pathlib import Path

# Try to load dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded environment variables from .env file")
except ImportError:
    print("⚠️  python-dotenv not installed")
    print("   Install with: pip install python-dotenv")
    print("   Continuing without .env file support...")
except Exception as e:
    print(f"⚠️  Could not load .env file: {e}")

print("")
print("🔍 Validating environment variables...")
print("=" * 70)

# Define required variables
REQUIRED_VARS = [
    ("GOOGLE_ACCOUNT_EMAIL", "Google account email for calendar operations"),
    ("GOOGLE_CALENDAR_ID", "Google Calendar ID"),
    ("GOOGLE_API_CREDENTIALS_FILE", "Path to Google API credentials file"),
]

# Define optional variables
OPTIONAL_VARS = [
    ("GOOGLE_TOKEN_FILE", "Path to OAuth token storage (auto-generated)"),
    ("GITHUB_TOKEN", "GitHub Personal Access Token"),
    ("GITHUB_REPO_OWNER", "GitHub repository owner"),
    ("GITHUB_REPO_NAME", "GitHub repository name"),
    ("APP_ENV", "Application environment"),
    ("TZ", "Timezone"),
]

missing_required = []
found_required = []
missing_optional = []
found_optional = []

# Check required variables
print("\n📋 Required Variables:")
print("-" * 70)

for var_name, description in REQUIRED_VARS:
    value = os.getenv(var_name)
    if value:
        found_required.append(var_name)
        # Mask the value for security
        if '@' in value:
            # Email address - show partial
            parts = value.split('@')
            masked = f"{parts[0][:2]}***@{parts[1]}"
            print(f"✅ {var_name:<30} = {masked}")
        elif value.endswith('.json') or value.endswith('.pickle'):
            # File path - show as is
            print(f"✅ {var_name:<30} = {value}")
        else:
            # Other values - show [SET]
            print(f"✅ {var_name:<30} = [SET]")
        print(f"   {description}")
    else:
        missing_required.append(var_name)
        print(f"❌ {var_name:<30} = [NOT SET]")
        print(f"   {description}")
    print()

# Check optional variables
print("\n📋 Optional Variables:")
print("-" * 70)

for var_name, description in OPTIONAL_VARS:
    value = os.getenv(var_name)
    if value:
        found_optional.append(var_name)
        # Mask sensitive values
        if var_name == "GITHUB_TOKEN":
            masked = f"{value[:7]}***{value[-4:]}" if len(value) > 11 else "[SET]"
            print(f"✅ {var_name:<30} = {masked}")
        else:
            print(f"✅ {var_name:<30} = {value}")
        print(f"   {description}")
    else:
        missing_optional.append(var_name)
        print(f"⚪ {var_name:<30} = [NOT SET]")
        print(f"   {description}")
    print()

# Check if credentials file exists
print("\n📋 File Existence Checks:")
print("-" * 70)

creds_file = os.getenv("GOOGLE_API_CREDENTIALS_FILE", "credentials.json")
if os.path.exists(creds_file):
    print(f"✅ Credentials file exists: {creds_file}")
    # Check file permissions
    try:
        import stat
        st = os.stat(creds_file)
        mode = st.st_mode
        perms = stat.filemode(mode)
        print(f"   Permissions: {perms}")
        
        # Check if world-readable or group-readable
        if mode & stat.S_IRWXO:
            print(f"   ⚠️  WARNING: File has overly permissive permissions!")
            print(f"   Run: chmod 600 {creds_file}")
        else:
            print(f"   ✅ File permissions are secure")
    except Exception as e:
        print(f"   ⚠️  Could not check permissions: {e}")
else:
    print(f"❌ Credentials file NOT found: {creds_file}")
    print(f"   Download from Google Cloud Console")
    print(f"   See: SETUP_GOOGLE_SERVICES_SECURE.md (INTERNAL ONLY)")

token_file = os.getenv("GOOGLE_TOKEN_FILE", "token.pickle")
if os.path.exists(token_file):
    print(f"✅ Token file exists: {token_file} (auto-generated)")
else:
    print(f"⚪ Token file not found: {token_file}")
    print(f"   (Will be generated on first authentication)")

print()

# Check .env file
if os.path.exists(".env"):
    print("✅ .env file exists")
    
    # Check if .env is in .gitignore
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            gitignore_content = f.read()
            if ".env" in gitignore_content:
                print("✅ .env is protected by .gitignore")
            else:
                print("⚠️  WARNING: .env NOT in .gitignore!")
                print("   Add to .gitignore immediately!")
    else:
        print("⚠️  .gitignore not found")
else:
    print("⚪ .env file not found")
    print("   Create from template: cp .env.example .env")
    print("   Or run: ./setup_google_calendar_secure.sh")

print()

# Summary
print("=" * 70)
print("📊 VALIDATION SUMMARY")
print("=" * 70)
print()

if missing_required:
    print(f"❌ FAILED: {len(missing_required)} required variable(s) missing:")
    for var in missing_required:
        print(f"   • {var}")
    print()
    print("🔧 How to fix:")
    print("   1. Create .env file: cp .env.example .env")
    print("   2. Or run setup: ./setup_google_calendar_secure.sh")
    print("   3. Configure missing variables in .env")
    print()
    print("📚 Documentation:")
    print("   • Setup guide: SETUP_GOOGLE_SERVICES_SECURE.md (INTERNAL ONLY)")
    print("   • Template: .env.example")
    print()
    sys.exit(1)
else:
    print(f"✅ PASSED: All {len(found_required)} required variables are set")
    print()
    
    if missing_optional:
        print(f"⚪ Optional: {len(missing_optional)} optional variable(s) not set:")
        for var in missing_optional:
            print(f"   • {var}")
        print()
    
    if found_optional:
        print(f"✅ Optional: {len(found_optional)} optional variable(s) configured")
        print()
    
    print("🎉 Environment configuration is valid!")
    print()
    print("🚀 You can now use Google Calendar integration:")
    print("   python3 import_calendar_to_google.py --calendar-file YOUR_FILE.ics")
    print()
    sys.exit(0)
