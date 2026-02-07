#!/usr/bin/env python3
"""
BGC Event Dashboard - System Test
Tests the integration between QR codes, GitHub issues, and the dashboard monitor.
"""

import os
import sys
import time
from datetime import datetime

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def print_status(message, status="info"):
    """Print a formatted status message."""
    icons = {
        "success": "✓",
        "error": "✗",
        "warning": "⚠",
        "info": "ℹ"
    }
    colors = {
        "success": "\033[0;32m",
        "error": "\033[0;31m",
        "warning": "\033[1;33m",
        "info": "\033[0;34m"
    }
    reset = "\033[0m"
    
    icon = icons.get(status, "•")
    color = colors.get(status, "")
    print(f"{color}{icon} {message}{reset}")

def test_python_version():
    """Test Python version is 3.8+."""
    print_section("TEST 1: Python Version")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print(f"Python version: {version_str}")
    
    if version.major >= 3 and version.minor >= 8:
        print_status(f"Python {version_str} is compatible", "success")
        return True
    else:
        print_status(f"Python {version_str} is too old. Need 3.8+", "error")
        return False

def test_dependencies():
    """Test required dependencies are installed."""
    print_section("TEST 2: Dependencies")
    
    dependencies = ["requests"]
    all_installed = True
    
    for dep in dependencies:
        try:
            __import__(dep)
            print_status(f"Module '{dep}' is installed", "success")
        except ImportError:
            print_status(f"Module '{dep}' is NOT installed", "error")
            print(f"  Install with: pip3 install {dep}")
            all_installed = False
    
    return all_installed

def test_project_files():
    """Test required project files exist."""
    print_section("TEST 3: Project Files")
    
    required_files = [
        "event_status_monitor.py",
        "generate_qr_codes.py",
        "ISSUE_TEMPLATE/enrollment-inquiry.md",
        "BGC_EVENT_DASHBOARD_INTEGRATION.md",
        "EVENT_DAY_DASHBOARD_README.md"
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print_status(f"Found: {file}", "success")
        else:
            print_status(f"Missing: {file}", "error")
            all_exist = False
    
    return all_exist

def test_github_token():
    """Test GitHub token is available."""
    print_section("TEST 4: GitHub Token")
    
    token = os.environ.get("GITHUB_TOKEN")
    
    if token:
        masked_token = token[:8] + "..." + token[-4:]
        print_status(f"GITHUB_TOKEN found: {masked_token}", "success")
        return True
    else:
        print_status("GITHUB_TOKEN not set", "warning")
        print("\nTo set GitHub token:")
        print("  export GITHUB_TOKEN=your_token_here")
        print("\nOR pass directly to script:")
        print("  python3 event_status_monitor.py --token YOUR_TOKEN")
        return False

def test_github_connection():
    """Test GitHub API connection."""
    print_section("TEST 5: GitHub API Connection")
    
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print_status("Skipping connection test (no token)", "warning")
        return False
    
    try:
        from event_status_monitor import GitHubAPIClient
        
        client = GitHubAPIClient(token, "smit4786", "DetroitAutomationAcademy")
        success, message = client.test_connection()
        
        if success:
            print_status(message, "success")
            return True
        else:
            print_status(message, "error")
            return False
    except Exception as e:
        print_status(f"Connection test failed: {str(e)}", "error")
        return False

def test_enrollment_fetch():
    """Test fetching enrollment issues."""
    print_section("TEST 6: Enrollment Data Fetch")
    
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print_status("Skipping data fetch test (no token)", "warning")
        return False
    
    try:
        from event_status_monitor import GitHubAPIClient
        
        client = GitHubAPIClient(token, "smit4786", "DetroitAutomationAcademy")
        issues = client.get_enrollment_issues()
        
        print_status(f"Successfully fetched {len(issues)} enrollment issues", "success")
        
        if len(issues) > 0:
            print(f"\nSample enrollment:")
            latest = issues[0]
            print(f"  Title: {latest['title']}")
            print(f"  Number: #{latest['number']}")
            print(f"  Created: {latest['created_at']}")
            print(f"  URL: {latest['html_url']}")
        
        return True
    except Exception as e:
        print_status(f"Failed to fetch enrollments: {str(e)}", "error")
        return False

def test_qr_code_generation():
    """Test QR code generation script."""
    print_section("TEST 7: QR Code Generation")
    
    if not os.path.exists("generate_qr_codes.py"):
        print_status("generate_qr_codes.py not found", "error")
        return False
    
    print_status("QR code generation script found", "success")
    print("\nTo test QR code generation:")
    print("  python3 generate_qr_codes.py --all-configs")
    print("\nQR codes link to:")
    print("  https://github.com/smit4786/DetroitAutomationAcademy/issues/new?template=enrollment-inquiry.md")
    
    return True

def test_dashboard_display():
    """Test dashboard can display data."""
    print_section("TEST 8: Dashboard Display")
    
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print_status("Skipping display test (no token)", "warning")
        return False
    
    try:
        from event_status_monitor import GitHubAPIClient, StatisticsCalculator, DisplayFormatter
        
        client = GitHubAPIClient(token, "smit4786", "DetroitAutomationAcademy")
        issues = client.get_enrollment_issues()
        stats = StatisticsCalculator.calculate_stats(issues, "2026-02-03")
        
        print_status("Statistics calculated successfully", "success")
        print(f"\nQuick summary:")
        print(f"  Total enrollments: {stats.total_enrollments}")
        print(f"  Today's enrollments: {stats.today_enrollments}")
        print(f"  Hourly rate: {stats.hourly_rate:.1f}/hour")
        
        if stats.program_breakdown:
            print(f"\nTop program: {max(stats.program_breakdown, key=stats.program_breakdown.get)}")
        
        return True
    except Exception as e:
        print_status(f"Display test failed: {str(e)}", "error")
        import traceback
        traceback.print_exc()
        return False

def run_all_tests():
    """Run all tests and report results."""
    print("\n" + "█"*70)
    print("  BGC EVENT DASHBOARD - SYSTEM TEST SUITE")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("█"*70)
    
    tests = [
        ("Python Version", test_python_version),
        ("Dependencies", test_dependencies),
        ("Project Files", test_project_files),
        ("GitHub Token", test_github_token),
        ("GitHub Connection", test_github_connection),
        ("Enrollment Fetch", test_enrollment_fetch),
        ("QR Code Generation", test_qr_code_generation),
        ("Dashboard Display", test_dashboard_display)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print_status(f"Test '{name}' crashed: {str(e)}", "error")
            results.append((name, False))
    
    # Summary
    print_section("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "success" if result else "error"
        print_status(f"{name}: {'PASSED' if result else 'FAILED'}", status)
    
    print(f"\n{'='*70}")
    print(f"  OVERALL: {passed}/{total} tests passed ({passed/total*100:.0f}%)")
    print(f"{'='*70}\n")
    
    if passed == total:
        print_status("✨ All tests passed! System is ready for deployment.", "success")
        print("\nNext steps:")
        print("  1. Launch staff terminal:")
        print("     python3 event_status_monitor.py --token $GITHUB_TOKEN --continuous --notify")
        print("\n  2. Launch large display:")
        print("     python3 event_status_monitor.py --token $GITHUB_TOKEN --continuous --display-mode")
        print("\n  3. See EVENT_DAY_DASHBOARD_README.md for full instructions")
        return 0
    else:
        print_status("⚠ Some tests failed. Fix issues before deployment.", "warning")
        print("\nSee BGC_EVENT_DASHBOARD_INTEGRATION.md for troubleshooting.")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
