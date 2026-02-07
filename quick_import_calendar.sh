#!/bin/bash

# Quick Calendar Import Script for BGC Event
# Opens Google Calendar import page and prepares the file

ICS_FILE="BGC_EVENT_READY_CALENDAR.ics"
CALENDAR_URL="https://calendar.google.com/calendar/u/0/r/settings/importexport"

echo "🚀 BGC Event - Quick Calendar Import"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📄 Event File: $ICS_FILE"
echo "📍 File Location: $(pwd)/$ICS_FILE"
echo ""

# Verify file exists
if [ ! -f "$ICS_FILE" ]; then
    echo "❌ Error: $ICS_FILE not found!"
    exit 1
fi

echo "✅ ICS file verified and ready"
echo ""
echo "🌐 Opening Google Calendar Import page..."
echo ""

# Open Calendar import page in default browser
open "$CALENDAR_URL"

echo "═══════════════════════════════════════════════════════════════"
echo "📋 NEXT STEPS:"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "In the browser window that just opened:"
echo ""
echo "1. Click the 'Import' tab (if not already selected)"
echo "2. Click 'Select file from your computer'"
echo "3. Navigate to:"
echo "   $(pwd)"
echo "4. Select: BGC_EVENT_READY_CALENDAR.ics"
echo "5. Choose calendar: 'Detroit Automation Academy'"
echo "6. Click 'Import'"
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✨ Alternative: Quick File Open"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Or simply double-click the ICS file to open with Calendar app:"
echo ""

# Also reveal the file in Finder for easy access
open -R "$ICS_FILE"

echo "✅ File location revealed in Finder"
echo ""
echo "🎯 Double-click '$ICS_FILE' to add directly to calendar!"
echo ""
echo "═══════════════════════════════════════════════════════════════"

