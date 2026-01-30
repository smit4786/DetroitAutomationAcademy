#!/usr/bin/env python3
"""
Detroit Automation Academy - Expense Tracking & Budget Sync
Automatically categorizes and syncs academy expenses to Google Sheets budget
"""

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import json
import csv
from pathlib import Path

# ========== CONFIGURATION ==========

SPREADSHEET_ID = "YOUR_DAA_BUDGET_SHEET_ID"  # Replace with actual Sheet ID
SERVICE_ACCOUNT_JSON = os.path.expanduser("~/.config/daa_expenses/service_account.json")
LOG_DIR = os.path.expanduser("~/.config/daa_expenses")

# Category mapping for auto-categorization
CATEGORY_MAP = {
    # Program Delivery - Materials & Supplies
    "arduino": "Program Delivery - Materials",
    "breadboard": "Program Delivery - Materials",
    "microcontroller": "Program Delivery - Materials",
    "resistor": "Program Delivery - Materials",
    "sensor": "Program Delivery - Materials",
    "led": "Program Delivery - Materials",
    "filament": "Program Delivery - Materials",
    "robotics kit": "Program Delivery - Materials",
    "3d print": "Program Delivery - Materials",
    
    # Program Delivery - Equipment
    "laser cutter": "Program Delivery - Equipment",
    "3d printer": "Program Delivery - Equipment",
    "soldering": "Program Delivery - Equipment",
    "oscilloscope": "Program Delivery - Equipment",
    "multimeter": "Program Delivery - Equipment",
    "workbench": "Program Delivery - Equipment",
    
    # Program Delivery - Instructor Compensation
    "instructor": "Program Delivery - Instructors",
    "facilitator": "Program Delivery - Instructors",
    "ta salary": "Program Delivery - Instructors",
    "teaching": "Program Delivery - Instructors",
    "speaker": "Program Delivery - Instructors",
    
    # Facility Costs
    "lab space": "Facility Costs",
    "workshop": "Facility Costs",
    "rent": "Facility Costs",
    "utilities": "Facility Costs",
    "internet": "Facility Costs",
    "facility insurance": "Facility Costs",
    
    # Technology & Software
    "google workspace": "Technology - Software",
    "github": "Technology - Software",
    "vimeo": "Technology - Software",
    "software": "Technology - Software",
    "cloud": "Technology - Software",
    "subscription": "Technology - Software",
    
    # Administrative
    "legal": "Administrative",
    "accounting": "Administrative",
    "professional services": "Administrative",
    "tax": "Administrative",
    "insurance": "Administrative",
    "compliance": "Administrative",
    
    # Office Operations
    "office supplies": "Office Operations",
    "printing": "Office Operations",
    "postage": "Office Operations",
    "supplies": "Office Operations",
    
    # Marketing
    "marketing": "Marketing & Outreach",
    "advertising": "Marketing & Outreach",
    "social media": "Marketing & Outreach",
    "brochure": "Marketing & Outreach",
    "event": "Marketing & Outreach",
    "promotion": "Marketing & Outreach",
    "print": "Marketing & Outreach",
}

# ========== FUNCTIONS ==========

def setup_logging():
    """Ensure log directory exists"""
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

def log_sync(message):
    """Write to sync log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(LOG_DIR, "expense_sync_log.txt")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def get_sheets_client():
    """Authenticate with Google Sheets API"""
    try:
        if not os.path.exists(SERVICE_ACCOUNT_JSON):
            log_sync(f"❌ ERROR: Service account file not found at {SERVICE_ACCOUNT_JSON}")
            log_sync("   Run GOOGLE_CLOUD_WALKTHROUGH.md steps 1-5 first")
            return None
        
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_JSON, scopes=scopes)
        client = gspread.authorize(creds)
        log_sync("✅ Authenticated with Google Sheets API")
        return client
    
    except Exception as e:
        log_sync(f"❌ Authentication failed: {str(e)}")
        return None

def categorize_expense(description):
    """
    Auto-categorize expense based on description
    Uses fuzzy matching on keywords
    """
    description_lower = description.lower()
    
    for keyword, category in CATEGORY_MAP.items():
        if keyword in description_lower:
            return category
    
    return "Uncategorized"

def sync_expenses():
    """Main sync function - reads expenses and updates budget"""
    setup_logging()
    log_sync("=" * 60)
    log_sync("🚀 STARTING DAA EXPENSE SYNC")
    log_sync(f"📅 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_sync("=" * 60)
    
    # Authenticate
    client = get_sheets_client()
    if not client:
        log_sync("❌ Cannot proceed without authentication")
        return False
    
    try:
        # Open spreadsheet
        sheet = client.open_by_key(SPREADSHEET_ID)
        log_sync(f"✅ Opened spreadsheet: {sheet.title}")
        
        # Get worksheet names
        worksheets = sheet.worksheets()
        worksheet_names = [ws.title for ws in worksheets]
        log_sync(f"📋 Available worksheets: {', '.join(worksheet_names)}")
        
        # Try to find expense worksheet
        expense_ws_name = None
        for name in ["Expenses", "DAA Expenses", "Academy Expenses", "Expense Tracker"]:
            if name in worksheet_names:
                expense_ws_name = name
                break
        
        if not expense_ws_name:
            log_sync(f"⚠️  Expense worksheet not found. Expected one of:")
            log_sync(f"   - Expenses")
            log_sync(f"   - DAA Expenses")
            log_sync(f"   - Academy Expenses")
            log_sync(f"   - Expense Tracker")
            log_sync(f"📝 Available: {', '.join(worksheet_names)}")
            return False
        
        expense_ws = sheet.worksheet(expense_ws_name)
        log_sync(f"✅ Reading from worksheet: {expense_ws_name}")
        
        # Get all expense data
        all_records = expense_ws.get_all_records()
        log_sync(f"📊 Found {len(all_records)} records")
        
        if not all_records:
            log_sync("⚠️  No expense records found")
            return False
        
        # Process expenses by category
        category_totals = {}
        processed_count = 0
        
        for record in all_records:
            # Skip empty rows
            if not any(record.values()):
                continue
            
            # Extract description and amount
            description = record.get("Description") or record.get("description") or ""
            amount_str = record.get("Amount") or record.get("amount") or "0"
            
            if not description or amount_str == "0":
                continue
            
            try:
                amount = float(str(amount_str).replace("$", "").replace(",", ""))
            except (ValueError, AttributeError):
                log_sync(f"⚠️  Skipping record - invalid amount: {amount_str}")
                continue
            
            # Categorize
            category = categorize_expense(description)
            
            # Aggregate by category
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += amount
            processed_count += 1
        
        log_sync(f"✅ Processed {processed_count} expenses")
        
        # Report by category
        if category_totals:
            log_sync("\n📈 EXPENSE SUMMARY BY CATEGORY:")
            total_expenses = 0
            for category in sorted(category_totals.keys()):
                amount = category_totals[category]
                total_expenses += amount
                log_sync(f"  • {category}: ${amount:,.2f}")
            
            log_sync(f"\n💰 TOTAL: ${total_expenses:,.2f}")
        
        # Try to update budget worksheet
        budget_ws_names = ["Budget", "DAA Budget", "Budget Plan"]
        budget_ws = None
        
        for name in budget_ws_names:
            if name in worksheet_names:
                budget_ws = sheet.worksheet(name)
                log_sync(f"✅ Found budget worksheet: {name}")
                break
        
        if budget_ws and category_totals:
            log_sync("\n📝 Updating budget worksheet...")
            try:
                # Get budget data
                budget_data = budget_ws.get_all_records()
                
                # Update amounts (depends on your budget sheet structure)
                # This is a template - adjust based on your actual sheet layout
                for row_idx, budget_row in enumerate(budget_data, start=2):
                    category = budget_row.get("Category") or budget_row.get("category")
                    
                    if category and category in category_totals:
                        # Update "Actual" column
                        actual_col = None
                        for col_idx, header in enumerate(budget_data[0].keys(), start=1):
                            if "actual" in header.lower():
                                actual_col = col_idx
                                break
                        
                        if actual_col:
                            budget_ws.update_cell(row_idx, actual_col, category_totals[category])
                            log_sync(f"  ✅ Updated {category}: ${category_totals[category]:,.2f}")
            
            except Exception as e:
                log_sync(f"⚠️  Could not auto-update budget: {str(e)}")
                log_sync("   Manual update may be required")
        
        log_sync("\n✅ SYNC COMPLETE!")
        log_sync(f"📁 Log saved to: {os.path.join(LOG_DIR, 'expense_sync_log.txt')}")
        return True
    
    except gspread.exceptions.SpreadsheetNotFound:
        log_sync(f"❌ Spreadsheet not found. Check SPREADSHEET_ID: {SPREADSHEET_ID}")
        return False
    except Exception as e:
        log_sync(f"❌ Sync failed: {str(e)}")
        import traceback
        log_sync(f"   Traceback: {traceback.format_exc()}")
        return False

# ========== MAIN ==========

if __name__ == "__main__":
    success = sync_expenses()
    exit(0 if success else 1)
