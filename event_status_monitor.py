#!/usr/bin/env python3
"""
BGC Event Status Dashboard Monitor
Detroit Automation Academy - Event Day Real-Time Enrollment Tracking

This script monitors GitHub enrollment issues in real-time during the BGC event,
displaying summary statistics for event staff and sending notifications when
enrollment milestones are reached.

Usage:
    # Basic usage with GitHub token
    python3 event_status_monitor.py --token YOUR_GITHUB_TOKEN
    
    # With notifications enabled
    python3 event_status_monitor.py --token YOUR_GITHUB_TOKEN --notify
    
    # Continuous monitoring mode (refreshes every 30 seconds)
    python3 event_status_monitor.py --token YOUR_GITHUB_TOKEN --continuous
    
    # Display on projector/large screen
    python3 event_status_monitor.py --token YOUR_GITHUB_TOKEN --continuous --display-mode
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import requests
from dataclasses import dataclass
from collections import defaultdict

# Configuration
GITHUB_REPO_OWNER = "smit4786"
GITHUB_REPO_NAME = "DetroitAutomationAcademy"
ENROLLMENT_LABEL = "enrollment"
EVENT_START_DATE = "2026-02-04"  # Update to current event date

# Milestone thresholds for notifications
MILESTONES = [10, 25, 50, 75, 100]


@dataclass
class EnrollmentStats:
    """Data class for enrollment statistics."""
    total_enrollments: int
    today_enrollments: int
    hourly_rate: float
    program_breakdown: Dict[str, int]
    education_breakdown: Dict[str, int]
    experience_breakdown: Dict[str, int]
    recent_enrollments: List[Dict]
    hourly_breakdown: Dict[int, int]


class GitHubAPIClient:
    """GitHub API client for fetching enrollment issues."""
    
    def __init__(self, token: str, owner: str, repo: str):
        """
        Initialize GitHub API client.
        
        Args:
            token: GitHub personal access token
            owner: Repository owner username
            repo: Repository name
        """
        self.token = token
        self.owner = owner
        self.repo = repo
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def test_connection(self) -> Tuple[bool, str]:
        """
        Test GitHub API connection and token validity.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            url = f"{self.base_url}/repos/{self.owner}/{self.repo}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                repo_data = response.json()
                return True, f"✓ Connected to {repo_data['full_name']}"
            elif response.status_code == 401:
                return False, "✗ Authentication failed. Check your GitHub token."
            elif response.status_code == 404:
                return False, f"✗ Repository {self.owner}/{self.repo} not found."
            else:
                return False, f"✗ Unexpected error: {response.status_code}"
        except Exception as e:
            return False, f"✗ Connection error: {str(e)}"
    
    def get_enrollment_issues(self, since: Optional[str] = None) -> List[Dict]:
        """
        Fetch enrollment issues from GitHub.
        
        Args:
            since: ISO 8601 timestamp to filter issues created after this date
            
        Returns:
            List of issue dictionaries
        """
        url = f"{self.base_url}/repos/{self.owner}/{self.repo}/issues"
        params = {
            "labels": ENROLLMENT_LABEL,
            "state": "all",
            "per_page": 100
        }
        
        if since:
            params["since"] = since
        
        all_issues = []
        page = 1
        
        while True:
            params["page"] = page
            response = self.session.get(url, params=params)
            
            if response.status_code != 200:
                print(f"⚠ Warning: API request failed with status {response.status_code}")
                break
            
            issues = response.json()
            if not issues:
                break
            
            all_issues.extend(issues)
            
            # Check if there are more pages
            if "next" not in response.links:
                break
            
            page += 1
        
        return all_issues


class EnrollmentParser:
    """Parser for enrollment issue bodies."""
    
    @staticmethod
    def parse_issue_body(body: str) -> Dict[str, any]:
        """
        Parse enrollment form data from issue body.
        
        Args:
            body: Issue body text
            
        Returns:
            Dictionary of parsed enrollment data
        """
        data = {
            "name": None,
            "email": None,
            "phone": None,
            "programs": [],
            "education": None,
            "experience": None,
            "interest": None
        }
        
        if not body:
            return data
        
        lines = body.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # Section headers
            if line.startswith("## Full Name"):
                current_section = "name"
                continue
            elif line.startswith("## Email Address"):
                current_section = "email"
                continue
            elif line.startswith("## Phone Number"):
                current_section = "phone"
                continue
            elif line.startswith("## Program Interest"):
                current_section = "programs"
                continue
            elif line.startswith("## Educational Background"):
                current_section = "education"
                continue
            elif line.startswith("## Experience Level"):
                current_section = "experience"
                continue
            elif line.startswith("## Tell Us About Your Interest"):
                current_section = "interest"
                continue
            elif line.startswith("---"):
                current_section = None
                continue
            
            # Skip empty lines and section markers
            if not line or line.startswith("_") or line.startswith("**"):
                continue
            
            # Parse data based on current section
            if current_section == "name" and not line.startswith("#"):
                data["name"] = line
            elif current_section == "email" and not line.startswith("#"):
                data["email"] = line
            elif current_section == "phone" and not line.startswith("#"):
                data["phone"] = line
            elif current_section in ["programs", "education", "experience"]:
                if line.startswith("- [x]") or line.startswith("- [X]"):
                    value = line.replace("- [x]", "").replace("- [X]", "").strip()
                    if current_section == "programs":
                        data["programs"].append(value)
                    elif current_section == "education":
                        data["education"] = value
                    elif current_section == "experience":
                        data["experience"] = value
            elif current_section == "interest" and not line.startswith("#"):
                if data["interest"]:
                    data["interest"] += " " + line
                else:
                    data["interest"] = line
        
        return data


class StatisticsCalculator:
    """Calculate enrollment statistics."""
    
    @staticmethod
    def calculate_stats(issues: List[Dict], event_date: str) -> EnrollmentStats:
        """
        Calculate enrollment statistics from issues.
        
        Args:
            issues: List of enrollment issues
            event_date: Event start date (YYYY-MM-DD format)
            
        Returns:
            EnrollmentStats object with calculated statistics
        """
        total = len(issues)
        
        # Parse event date
        event_datetime = datetime.fromisoformat(event_date)
        today_start = event_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        
        # Count today's enrollments
        today_count = 0
        hourly_counts = defaultdict(int)
        recent = []
        
        # Breakdown counters
        program_counts = defaultdict(int)
        education_counts = defaultdict(int)
        experience_counts = defaultdict(int)
        
        for issue in issues:
            created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            
            # Count today's enrollments
            if today_start <= created_at < today_end:
                today_count += 1
                hour = created_at.hour
                hourly_counts[hour] += 1
            
            # Parse issue body for detailed stats
            parsed = EnrollmentParser.parse_issue_body(issue.get("body", ""))
            
            # Program interest breakdown
            for program in parsed["programs"]:
                program_counts[program] += 1
            
            # Education breakdown
            if parsed["education"]:
                education_counts[parsed["education"]] += 1
            
            # Experience breakdown
            if parsed["experience"]:
                experience_counts[parsed["experience"]] += 1
            
            # Recent enrollments (last 5)
            if len(recent) < 5:
                recent.append({
                    "title": issue["title"],
                    "created_at": issue["created_at"],
                    "number": issue["number"],
                    "url": issue["html_url"]
                })
        
        # Calculate hourly rate (enrollments per hour today)
        current_time = datetime.utcnow()
        hours_elapsed = max((current_time - today_start).total_seconds() / 3600, 0.1)
        hourly_rate = today_count / hours_elapsed if hours_elapsed > 0 else 0
        
        return EnrollmentStats(
            total_enrollments=total,
            today_enrollments=today_count,
            hourly_rate=hourly_rate,
            program_breakdown=dict(program_counts),
            education_breakdown=dict(education_counts),
            experience_breakdown=dict(experience_counts),
            recent_enrollments=recent,
            hourly_breakdown=dict(hourly_counts)
        )


class DisplayFormatter:
    """Format statistics for display."""
    
    @staticmethod
    def format_stats_terminal(stats: EnrollmentStats, display_mode: bool = False) -> str:
        """
        Format statistics for terminal display.
        
        Args:
            stats: EnrollmentStats object
            display_mode: If True, use larger formatting for projector display
            
        Returns:
            Formatted string for terminal output
        """
        if display_mode:
            return DisplayFormatter._format_display_mode(stats)
        else:
            return DisplayFormatter._format_compact_mode(stats)
    
    @staticmethod
    def _format_compact_mode(stats: EnrollmentStats) -> str:
        """Compact format for staff terminal."""
        output = []
        output.append("\n" + "="*70)
        output.append("🎓 DETROIT AUTOMATION ACADEMY - BGC EVENT ENROLLMENT DASHBOARD")
        output.append("="*70)
        output.append(f"📊 Updated: {datetime.now().strftime('%I:%M:%S %p')}")
        output.append("")
        
        # Key metrics
        output.append("📈 KEY METRICS")
        output.append("-" * 70)
        output.append(f"  Total Enrollments:        {stats.total_enrollments}")
        output.append(f"  Today's Enrollments:      {stats.today_enrollments}")
        output.append(f"  Hourly Rate:              {stats.hourly_rate:.1f} enrollments/hour")
        output.append("")
        
        # Program interest breakdown
        if stats.program_breakdown:
            output.append("🎯 PROGRAM INTEREST")
            output.append("-" * 70)
            for program, count in sorted(stats.program_breakdown.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / stats.total_enrollments * 100) if stats.total_enrollments > 0 else 0
                bar = "█" * int(percentage / 5)
                output.append(f"  {program:<30} {count:>3} ({percentage:>5.1f}%) {bar}")
            output.append("")
        
        # Education background
        if stats.education_breakdown:
            output.append("🎓 EDUCATION BACKGROUND")
            output.append("-" * 70)
            for edu, count in sorted(stats.education_breakdown.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / stats.total_enrollments * 100) if stats.total_enrollments > 0 else 0
                output.append(f"  {edu:<30} {count:>3} ({percentage:>5.1f}%)")
            output.append("")
        
        # Recent enrollments
        if stats.recent_enrollments:
            output.append("🆕 RECENT ENROLLMENTS (Last 5)")
            output.append("-" * 70)
            for enrollment in stats.recent_enrollments:
                created = datetime.strptime(enrollment["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                time_str = created.strftime("%I:%M %p")
                output.append(f"  #{enrollment['number']:<5} {time_str:<10} {enrollment['title']}")
            output.append("")
        
        # Hourly breakdown
        if stats.hourly_breakdown:
            output.append("⏰ HOURLY BREAKDOWN (Today)")
            output.append("-" * 70)
            for hour in sorted(stats.hourly_breakdown.keys()):
                count = stats.hourly_breakdown[hour]
                time_label = f"{hour:02d}:00"
                bar = "█" * count
                output.append(f"  {time_label}  {bar} ({count})")
            output.append("")
        
        output.append("="*70)
        return "\n".join(output)
    
    @staticmethod
    def _format_display_mode(stats: EnrollmentStats) -> str:
        """Large format for projector/display screen."""
        output = []
        output.append("\n" + "="*90)
        output.append(" " * 20 + "🎓 BGC EVENT - LIVE ENROLLMENT DASHBOARD")
        output.append("="*90)
        output.append("")
        output.append(" " * 30 + f"Updated: {datetime.now().strftime('%I:%M:%S %p')}")
        output.append("")
        output.append("")
        
        # Large key metrics
        output.append(" " * 25 + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        output.append("")
        output.append(" " * 25 + f"   TOTAL ENROLLMENTS:    {stats.total_enrollments:>4}")
        output.append("")
        output.append(" " * 25 + f"   TODAY'S ENROLLMENTS:  {stats.today_enrollments:>4}")
        output.append("")
        output.append(" " * 25 + f"   HOURLY RATE:          {stats.hourly_rate:>4.1f}/hr")
        output.append("")
        output.append(" " * 25 + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        output.append("")
        output.append("")
        
        # Program interest (top 3)
        if stats.program_breakdown:
            output.append(" " * 25 + "🎯 TOP PROGRAM INTERESTS")
            output.append("")
            for i, (program, count) in enumerate(sorted(stats.program_breakdown.items(), key=lambda x: x[1], reverse=True)[:3], 1):
                percentage = (count / stats.total_enrollments * 100) if stats.total_enrollments > 0 else 0
                output.append(" " * 25 + f"   {i}. {program:<30} {count:>3} ({percentage:>5.1f}%)")
            output.append("")
        
        output.append("="*90)
        return "\n".join(output)


class NotificationManager:
    """Manage milestone notifications."""
    
    def __init__(self):
        """Initialize notification manager."""
        self.notified_milestones = set()
    
    def check_milestones(self, current_count: int) -> List[int]:
        """
        Check if any milestones have been reached.
        
        Args:
            current_count: Current enrollment count
            
        Returns:
            List of newly reached milestones
        """
        new_milestones = []
        for milestone in MILESTONES:
            if current_count >= milestone and milestone not in self.notified_milestones:
                new_milestones.append(milestone)
                self.notified_milestones.add(milestone)
        return new_milestones
    
    @staticmethod
    def display_milestone_notification(milestone: int):
        """
        Display milestone notification.
        
        Args:
            milestone: Milestone number reached
        """
        print("\n" + "🎉" * 40)
        print(f"\n   🎊 MILESTONE REACHED: {milestone} ENROLLMENTS! 🎊\n")
        print("🎉" * 40 + "\n")
        
        # Play system bell (if available)
        print("\a")  # ASCII bell character


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="BGC Event Enrollment Dashboard - Real-time monitoring"
    )
    parser.add_argument(
        "--token",
        type=str,
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--continuous",
        action="store_true",
        help="Continuous monitoring mode (refreshes every 30 seconds)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Refresh interval in seconds (default: 30)"
    )
    parser.add_argument(
        "--display-mode",
        action="store_true",
        help="Large display mode for projector/screen"
    )
    parser.add_argument(
        "--notify",
        action="store_true",
        help="Enable milestone notifications"
    )
    parser.add_argument(
        "--event-date",
        type=str,
        default=EVENT_START_DATE,
        help=f"Event date in YYYY-MM-DD format (default: {EVENT_START_DATE})"
    )
    
    args = parser.parse_args()
    
    # Get GitHub token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("❌ Error: GitHub token required.")
        print("\nProvide token via:")
        print("  1. --token argument: python3 event_status_monitor.py --token YOUR_TOKEN")
        print("  2. Environment variable: export GITHUB_TOKEN=YOUR_TOKEN")
        print("\nTo create a token:")
        print("  1. Go to https://github.com/settings/tokens")
        print("  2. Click 'Generate new token (classic)'")
        print("  3. Select scope: 'repo' (Full control of private repositories)")
        print("  4. Click 'Generate token' and copy the token")
        return 1
    
    # Initialize GitHub client
    client = GitHubAPIClient(token, GITHUB_REPO_OWNER, GITHUB_REPO_NAME)
    
    # Test connection
    print("🔌 Testing GitHub API connection...")
    success, message = client.test_connection()
    print(message)
    
    if not success:
        return 1
    
    # Initialize notification manager
    notifier = NotificationManager() if args.notify else None
    
    # Main monitoring loop
    try:
        iteration = 0
        while True:
            iteration += 1
            
            # Clear screen in continuous mode
            if args.continuous and iteration > 1:
                clear_screen()
            
            # Fetch enrollment issues
            print(f"📥 Fetching enrollment data... ", end="", flush=True)
            issues = client.get_enrollment_issues()
            print(f"Found {len(issues)} enrollments")
            
            # Calculate statistics
            stats = StatisticsCalculator.calculate_stats(issues, args.event_date)
            
            # Display statistics
            output = DisplayFormatter.format_stats_terminal(stats, args.display_mode)
            print(output)
            
            # Check milestones
            if notifier:
                new_milestones = notifier.check_milestones(stats.total_enrollments)
                for milestone in new_milestones:
                    NotificationManager.display_milestone_notification(milestone)
            
            # Exit if not continuous mode
            if not args.continuous:
                break
            
            # Wait for next refresh
            print(f"\n⏳ Next update in {args.interval} seconds... (Ctrl+C to stop)")
            time.sleep(args.interval)
            
    except KeyboardInterrupt:
        print("\n\n👋 Monitoring stopped by user.")
        return 0
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
