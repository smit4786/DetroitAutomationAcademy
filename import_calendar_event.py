#!/usr/bin/env python3
"""
Import ICS event to Detroit Automation Academy Google Calendar
Uses Google Calendar API to import BGC_EVENT_READY_CALENDAR.ics
"""

import os
import sys
from datetime import datetime
from icalendar import Calendar
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    """Get valid user credentials from storage or run OAuth flow."""
    creds = None
    token_path = 'token.pickle'
    
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Try to use gcloud credentials
            try:
                from google.auth import default
                creds, project = default(scopes=SCOPES)
                print("✅ Using gcloud default credentials")
            except Exception as e:
                print(f"❌ Error getting credentials: {e}")
                print("\nPlease run: gcloud auth application-default login")
                sys.exit(1)
        
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def parse_ics_file(filename):
    """Parse ICS file and extract event details."""
    with open(filename, 'rb') as f:
        cal = Calendar.from_ical(f.read())
    
    for component in cal.walk():
        if component.name == "VEVENT":
            event_data = {
                'summary': str(component.get('summary')),
                'description': str(component.get('description')),
                'location': str(component.get('location')),
                'start': component.get('dtstart').dt,
                'end': component.get('dtend').dt,
                'attendees': [],
                'reminders': []
            }
            
            # Parse attendees
            attendees = component.get('attendee')
            if attendees:
                if isinstance(attendees, list):
                    for attendee in attendees:
                        email = str(attendee).replace('mailto:', '')
                        event_data['attendees'].append({'email': email})
                else:
                    email = str(attendees).replace('mailto:', '')
                    event_data['attendees'].append({'email': email})
            
            # Parse reminders (alarms)
            for subcomponent in component.walk():
                if subcomponent.name == 'VALARM':
                    trigger = subcomponent.get('trigger')
                    if trigger:
                        # Convert trigger to minutes
                        trigger_str = str(trigger)
                        if 'P1D' in trigger_str:
                            event_data['reminders'].append({'method': 'popup', 'minutes': 1440})
                        elif 'PT1H' in trigger_str:
                            event_data['reminders'].append({'method': 'popup', 'minutes': 60})
                        elif 'PT15M' in trigger_str:
                            event_data['reminders'].append({'method': 'popup', 'minutes': 15})
            
            return event_data
    
    return None

def import_event_to_calendar(service, event_data, calendar_id='primary'):
    """Import event to Google Calendar."""
    
    # Convert datetime to RFC3339 format
    start_time = event_data['start']
    end_time = event_data['end']
    
    # Format datetime properly
    if isinstance(start_time, datetime):
        start_str = start_time.isoformat()
        end_str = end_time.isoformat()
        time_zone = 'America/Detroit'
    else:
        # Date only
        start_str = start_time.isoformat()
        end_str = end_time.isoformat()
        time_zone = None
    
    event = {
        'summary': event_data['summary'],
        'location': event_data['location'],
        'description': event_data['description'],
        'start': {
            'dateTime': start_str,
            'timeZone': time_zone,
        },
        'end': {
            'dateTime': end_str,
            'timeZone': time_zone,
        },
        'attendees': event_data['attendees'],
        'reminders': {
            'useDefault': False,
            'overrides': event_data['reminders'],
        },
    }
    
    try:
        created_event = service.events().insert(calendarId=calendar_id, body=event, sendUpdates='all').execute()
        return created_event
    except HttpError as error:
        print(f'❌ An error occurred: {error}')
        return None

def list_calendars(service):
    """List all available calendars."""
    try:
        calendar_list = service.calendarList().list().execute()
        calendars = calendar_list.get('items', [])
        
        print("\n📅 Available Calendars:")
        print("-" * 80)
        for cal in calendars:
            print(f"  • {cal['summary']}")
            print(f"    ID: {cal['id']}")
            print(f"    Access Role: {cal.get('accessRole', 'N/A')}")
            print()
        
        return calendars
    except HttpError as error:
        print(f'❌ Error listing calendars: {error}')
        return []

def find_calendar_by_name(service, name):
    """Find calendar by name."""
    calendars = list_calendars(service)
    for cal in calendars:
        if name.lower() in cal['summary'].lower():
            return cal['id']
    return None

def main():
    """Main function to import ICS file to Google Calendar."""
    print("🚀 BGC Event Calendar Import Tool")
    print("=" * 80)
    
    ics_file = 'BGC_EVENT_READY_CALENDAR.ics'
    
    if not os.path.exists(ics_file):
        print(f"❌ Error: {ics_file} not found!")
        sys.exit(1)
    
    print(f"📄 Parsing ICS file: {ics_file}")
    event_data = parse_ics_file(ics_file)
    
    if not event_data:
        print("❌ Error: Could not parse event from ICS file")
        sys.exit(1)
    
    print(f"✅ Event parsed successfully:")
    print(f"   Title: {event_data['summary']}")
    print(f"   Date: {event_data['start']}")
    print(f"   Location: {event_data['location']}")
    print(f"   Attendees: {len(event_data['attendees'])}")
    print(f"   Reminders: {len(event_data['reminders'])}")
    print()
    
    print("🔐 Authenticating with Google Calendar...")
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    
    # Look for Detroit Automation Academy calendar
    print("\n🔍 Looking for 'Detroit Automation Academy' calendar...")
    calendar_id = find_calendar_by_name(service, 'Detroit Automation Academy')
    
    if not calendar_id:
        print("⚠️  Could not find 'Detroit Automation Academy' calendar")
        print("   Importing to primary calendar instead...")
        calendar_id = 'primary'
    else:
        print(f"✅ Found calendar: {calendar_id}")
    
    print(f"\n📤 Importing event to Google Calendar...")
    created_event = import_event_to_calendar(service, event_data, calendar_id)
    
    if created_event:
        print("\n" + "=" * 80)
        print("✅ SUCCESS! Event imported to Google Calendar")
        print("=" * 80)
        print(f"Event ID: {created_event['id']}")
        print(f"Event Link: {created_event.get('htmlLink', 'N/A')}")
        print(f"Status: {created_event.get('status', 'N/A').upper()}")
        print(f"Created: {created_event.get('created', 'N/A')}")
        print(f"Updated: {created_event.get('updated', 'N/A')}")
        print("\n📧 Calendar invites sent to attendees:")
        for attendee in event_data['attendees']:
            print(f"   • {attendee['email']}")
        print("\n⏰ Reminders configured:")
        for reminder in event_data['reminders']:
            minutes = reminder['minutes']
            if minutes >= 1440:
                print(f"   • {minutes // 1440} day(s) before")
            elif minutes >= 60:
                print(f"   • {minutes // 60} hour(s) before")
            else:
                print(f"   • {minutes} minute(s) before")
        print("\n🎉 Event is now LIVE on the calendar!")
        print("=" * 80)
    else:
        print("\n❌ Failed to import event")
        sys.exit(1)

if __name__ == '__main__':
    main()
