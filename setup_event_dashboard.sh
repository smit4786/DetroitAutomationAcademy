#!/bin/bash
# BGC Event Dashboard - Quick Setup Script
# This script prepares the event dashboard system for deployment

set -e  # Exit on error

echo "=========================================="
echo "BGC EVENT DASHBOARD - QUICK SETUP"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}[1/5] Checking Python version...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓ Python 3 found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 not found. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Check if we're in the right directory
echo ""
echo -e "${BLUE}[2/5] Verifying project directory...${NC}"
if [ -f "event_status_monitor.py" ]; then
    echo -e "${GREEN}✓ Found event_status_monitor.py${NC}"
else
    echo -e "${RED}✗ event_status_monitor.py not found.${NC}"
    echo "Please run this script from the DetroitAutomationAcademy directory."
    exit 1
fi

# Install dependencies
echo ""
echo -e "${BLUE}[3/5] Installing dependencies...${NC}"
if pip3 install requests &> /dev/null; then
    echo -e "${GREEN}✓ Installed: requests${NC}"
else
    echo -e "${YELLOW}⚠ Could not install requests. You may need to install it manually.${NC}"
    echo "  Try: pip3 install requests"
fi

# Check for GitHub token
echo ""
echo -e "${BLUE}[4/5] Checking GitHub token...${NC}"
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}⚠ GITHUB_TOKEN environment variable not set${NC}"
    echo ""
    echo "To create a GitHub token:"
    echo "  1. Go to: https://github.com/settings/tokens"
    echo "  2. Click 'Generate new token (classic)'"
    echo "  3. Select scope: 'repo'"
    echo "  4. Copy the token"
    echo ""
    echo "Then set it:"
    echo "  export GITHUB_TOKEN=your_token_here"
    echo ""
    read -p "Do you want to set your GitHub token now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -sp "Paste your GitHub token: " TOKEN
        echo ""
        export GITHUB_TOKEN=$TOKEN
        
        # Offer to save permanently
        read -p "Save token to ~/.bashrc for future use? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "export GITHUB_TOKEN=$TOKEN" >> ~/.bashrc
            echo -e "${GREEN}✓ Token saved to ~/.bashrc${NC}"
        fi
    fi
else
    echo -e "${GREEN}✓ GITHUB_TOKEN is set${NC}"
fi

# Test connection
echo ""
echo -e "${BLUE}[5/5] Testing GitHub API connection...${NC}"
if [ ! -z "$GITHUB_TOKEN" ]; then
    python3 event_status_monitor.py --token $GITHUB_TOKEN 2>&1 | head -3
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Dashboard is ready!${NC}"
    else
        echo -e "${YELLOW}⚠ Connection test completed (check output above)${NC}"
    fi
else
    echo -e "${YELLOW}⚠ Skipping connection test (no token provided)${NC}"
    echo "Run manually: python3 event_status_monitor.py --token YOUR_TOKEN"
fi

# Print next steps
echo ""
echo "=========================================="
echo -e "${GREEN}SETUP COMPLETE!${NC}"
echo "=========================================="
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "1. STAFF TERMINAL (registration desk):"
echo "   python3 event_status_monitor.py --token \$GITHUB_TOKEN --continuous --notify"
echo ""
echo "2. LARGE DISPLAY (projector/TV):"
echo "   python3 event_status_monitor.py --token \$GITHUB_TOKEN --continuous --display-mode"
echo ""
echo "3. TEST WITH ONE-TIME SNAPSHOT:"
echo "   python3 event_status_monitor.py --token \$GITHUB_TOKEN"
echo ""
echo "📚 DOCUMENTATION:"
echo "   - Quick Start:     EVENT_DAY_DASHBOARD_README.md"
echo "   - Full Guide:      BGC_EVENT_DASHBOARD_INTEGRATION.md"
echo "   - QR Codes:        QR_CODE_DEPLOYMENT.md"
echo ""
echo "❓ HELP:"
echo "   - Troubleshooting: See BGC_EVENT_DASHBOARD_INTEGRATION.md"
echo "   - Support:         (313) 306-3767"
echo ""
echo "✨ You're ready for the BGC event! Good luck! 🎉"
echo ""
