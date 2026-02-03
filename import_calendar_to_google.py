#!/usr/bin/env python3
"""
Google Calendar Importer for Detroit Automation Academy Events
Imports BGC_EVENT_DAY2_CALENDAR.ics to Google Calendar via API

Usage:
    python3 import_calendar_to_google.py \
        --calendar-file BGC_EVENT_DAY2_CALENDAR.ics \
        --calendar-name "Detroit Automation Academy"

Requirements:
    - google-auth-oauthlib
    - google-auth-httplib2
    - google-api-python-client

Setup:
    1. Create Google Cloud Project
    2. Enable Google Calendar API
    3. Create OAuth 2.0 credentials (Desktop app)
    4. Download credentials.json to workspace
    5. Run script (will prompt for authorization first time)
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth import default
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("❌ Error: Google API libraries not installed")
    print("Install with: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

import icalendar
import json
from dateutil import parser as date_parser


class GoogleCalendarImporter:
    """Import ICS calendar events to Google Calendar"""

    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    def __init__(self, credentials_file="credentials.json"):
        self.credentials_file = credentials_file
        self.service = None
        self.calendar_id = None
        
    def authenticate(self):
        """Authenticate with Google Calendar API"""
        try:
            # Try service account first
            if os.path.exists(self.credentials_file):
                self.service = build("calendar", "v3", 
                    credentials=Credentials.from_service_account_file(
                        self.credentials_file, scopes=self.SCOPES))
                print("✅ Authenticated with service account")
                return
        except:
            pass

        try:
            # Fall back to OAuth 2.0 user authentication
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credentials_file, self.SCOPES)
            creds = flow.run_local_server(port=0)
            self.service = build("calendar", "v3", credentials=creds)
            print("✅ Authenticated with Google account")
        except FileNotFoundError:
            print("❌ Error: credentials.json not found")
            print("Please set up Google Calendar API credentials first")
            print("See README or https://developers.google.com/calendar/api/quickstart/python")
            sys.exit(1)

    def get_or_create_calendar(self, calendar_name):
        """Get calendar by name or create if doesn't exist"""
        try:
            # List existing calendars
            calendars = self.service.calendarList().list().execute()
            
            for item in calendars.get("items", []):
                if item["summary"] == calendar_name:
                    self.calendar_id = item["id"]
                    print(f"✅ Found calendar: {calendar_name} (ID: {self.calendar_id})")
                    return

            # Create new calendar if not found
            calendar_body = {
                "summary": calendar_name,
                "description": "Detroit Automation Academy Events",
                "timeZone": "America/New_York"
            }
            created = self.service.calendars().insert(body=calendar_body).execute()
            self.calendar_id = created["id"]
            print(f"✅ Created calendar: {calendar_name} (ID: {self.calendar_id})")

        except HttpError as error:
            print(f"❌ Error managing calendar: {error}")
            sys.exit(1)

    def import_ics_file(self, ics_file):
        """Parse ICS file and import events"""
        try:
            with open(ics_file, "rb") as f:
                cal = icalendar.Calendar.from_ical(f.read())
        except FileNotFoundError:
            print(f"❌ Error: ICS file not found: {ics_file}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error parsing ICS file: {e}")
            sys.exit(1)

        events = [comp for comp in cal.walk() if comp.name == "VEVENT"]
        print(f"📋 Found {len(events)} events in ICS file")

        if not events:
            print("⚠️  No events found in ICS file")
            return 0

        imported = 0
        for event in events:
            try:
                imported += self._import_event(event)
            except Exception as e:
                print(f"⚠️  Error importing event: {e}")
                continue

        return imported

    def _import_event(self, ics_event):
        """Convert and import single ICS event to Google Calendar"""
        try:
            # Extract event data
            summary = str(ics_event.get("summary", "Untitled Event"))
            description = str(ics_event.get("description", ""))
            location = str(ics_event.get("location", ""))
            
            start = ics_event.get("dtstart")
            end = ics_event.get("dtend")

            if not start or not end:
                print(f"⚠️  Skipping event without start/end time: {summary}")
                return 0

            # Convert to datetime objects
            if hasattr(start.dt, "hour"):  # Has time component
                start_time = start.dt
                end_time = end.dt
            else:  # All-day event
                start_time = start.dt
                end_time = end.dt

            # Build Google Calendar event
            google_event = {
                "summary": summary,
                "description": description,
                "location": location,
                "start": self._datetime_to_rfc3339(start_time),
                "end": self._datetime_to_rfc3339(end_time),
            }

            # Add organizer if present
            organizer = ics_event.get("organizer")
            if organizer:
                google_event["organizer"] = {
                    "email": str(organizer),
                    "displayName": self._extract_email(str(organizer))
                }

            # Add attendees if present
            attendees = ics_event.get("attendee")
            if attendees:
                if not isinstance(attendees, list):
                    attendees = [attendees]
                google_event["attendees"] = [
                    {"email": self._extract_email(str(att)), "responseStatus": "needsAction"}
                    for att in attendees
                ]

            # Insert into Google Calendar
            event = self.service.events().insert(
                calendarId=self.calendar_id,
                body=google_event,
                sendUpdates="eventCreator"
            ).execute()

            print(f"✅ Imported: {summary}")
            print(f"   Time: {start_time} → {end_time}")
            if attendees:
                print(f"   Attendees: {len(attendees)}")

            return 1

        except Exception as e:
            print(f"❌ Error importing event {ics_event.get('summary', 'Unknown')}: {e}")
            return 0

    @staticmethod
    def _extract_email(mailto_str):
        """Extract email from mailto: URI"""
        if "mailto:" in mailto_str:
            return mailto_str.split("mailto:")[-1].rstrip(">")
        return mailto_str.rstrip(">").lstrip("<")

    @staticmethod
    def _datetime_to_rfc3339(dt):
        """Convert datetime to RFC 3339 format for Google Calendar"""
        if hasattr(dt, "isoformat"):
            if hasattr(dt, "hour"):  # Has time component
                return {"dateTime": dt.isoformat(), "timeZone": "America/New_York"}
            else:  # All-day event
                return {"date": dt.isoformat()}
        return {"dateTime": str(dt)}


def main():
    parser = argparse.ArgumentParser(
        description="Import Detroit Automation Academy calendar events to Google Calendar",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Import with default settings
  python3 import_calendar_to_google.py

  # Specify calendar file
  python3 import_calendar_to_google.py --calendar-file BGC_EVENT_DAY2_CALENDAR.ics

  # Create custom calendar
  python3 import_calendar_to_google.py --calendar-name "DAA Events"

Setup Instructions:
  1. Create Google Cloud Project: https://console.cloud.google.com
  2. Enable Google Calendar API
  3. Create OAuth 2.0 Desktop credentials
  4. Download credentials.json to workspace
  5. Run this script (will open browser for authorization)
        """
    )

    parser.add_argument(
        "--calendar-file",
        default="BGC_EVENT_DAY2_CALENDAR.ics",
        help="Path to ICS calendar file (default: BGC_EVENT_DAY2_CALENDAR.ics)"
    )

    parser.add_argument(
        "--calendar-name",
        default="Detroit Automation Academy",
        help="Name of Google Calendar (creates if doesn't exist, default: Detroit Automation Academy)"
    )

    parser.add_argument(
        "--credentials",
        default="credentials.json",
        help="Path to Google credentials file (default: credentials.json)"
    )

    args = parser.parse_args()

    print("🚀 Detroit Automation Academy - Google Calendar Importer")
    print("=" * 60)

    # Verify ICS file exists
    if not os.path.exists(args.calendar_file):
        print(f"❌ Error: Calendar file not found: {args.calendar_file}")
        print(f"Current directory: {os.getcwd()}")
        sys.exit(1)

    print(f"📋 Calendar file: {args.calendar_file}")
    print(f"📅 Target calendar: {args.calendar_name}")
    print("=" * 60)

    # Initialize importer
    importer = GoogleCalendarImporter(args.credentials)

    # Authenticate
    print("\n🔐 Authenticating with Google Calendar API...")
    importer.authenticate()

    # Get or create calendar
    print(f"\n📅 Setting up calendar: {args.calendar_name}")
    importer.get_or_create_calendar(args.calendar_name)

    # Import events
    print(f"\n📥 Importing events from {args.calendar_file}...")
    imported = importer.import_ics_file(args.calendar_file)

    print("\n" + "=" * 60)
    if imported > 0:
        print(f"✅ SUCCESS: {imported} event(s) imported to Google Calendar")
        print(f"📅 Calendar: {args.calendar_name}")
        print(f"🔗 View at: https://calendar.google.com")
    else:
        print("❌ No events were imported")
        sys.exit(1)


if __name__ == "__main__":
    main()
