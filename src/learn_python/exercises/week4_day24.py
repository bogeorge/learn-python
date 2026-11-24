import sys
import json
from datetime import datetime, date, time, timedelta
import calendar
import os

"""
Week 4, Day 24: Dates & Times

Exercises to practice working with dates, times, and time intervals.
"""


def exercise_1_datetime_basics():
    """
    Basic datetime operations.

    1. Get current date and time
    2. Create specific dates and times
    3. Format dates and times
    4. Parse strings to datetime
    """
    print("Exercise 1: datetime Basics")
    print("-" * 40)

    # Current date and time
    now = datetime.now()
    today = date.today()
    current_time = now.time()

    print("Current date and time:")
    print(f"  Full datetime: {now}")
    print(f"  Date only: {today}")
    print(f"  Time only: {current_time}")
    print()

    # Creating specific dates and times
    specific_date = date(2024, 12, 25)
    specific_time = time(14, 30, 45)  # 2:30:45 PM
    specific_datetime = datetime(2024, 6, 15, 10, 0, 0)  # June 15, 2024 10:00 AM

    print("Specific dates and times:")
    print(f"  Christmas 2024: {specific_date}")
    print(f"  Time: {specific_time}")
    print(f"  Meeting: {specific_datetime}")
    print()

    # Formatting dates and times
    print("Formatted dates and times:")
    print(f"  ISO format: {now.isoformat()}")
    print(f"  Custom format: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")
    print(f"  Short date: {today.strftime('%m/%d/%Y')}")
    print(f"  Time only: {current_time.strftime('%H:%M:%S')}")
    print()

    # Parsing strings
    date_string = "2024-03-15"
    datetime_string = "March 15, 2024 14:30:00"

    parsed_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    parsed_datetime = datetime.strptime(datetime_string, "%B %d, %Y %H:%M:%S")

    print("Parsed dates:")
    print(f"  From '{date_string}': {parsed_date}")
    print(f"  From '{datetime_string}': {parsed_datetime}")


def exercise_2_date_arithmetic():
    """
    Date arithmetic and comparisons.

    1. Add/subtract days, hours, minutes
    2. Compare dates
    3. Calculate time differences
    4. Work with timedelta
    """
    print("\n\nExercise 2: Date Arithmetic")
    print("-" * 40)

    today = date.today()
    now = datetime.now()

    # Adding/subtracting days
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    yesterday = today - timedelta(days=1)

    print("Date arithmetic with days:")
    print(f"  Today: {today}")
    print(f"  Tomorrow: {tomorrow}")
    print(f"  Next week: {next_week}")
    print(f"  Yesterday: {yesterday}")
    print()

    # Adding/subtracting time
    one_hour_later = now + timedelta(hours=1)
    thirty_minutes_ago = now - timedelta(minutes=30)
    two_days_three_hours = now + timedelta(days=2, hours=3)

    print("Time arithmetic:")
    print(f"  Now: {now.strftime('%H:%M:%S')}")
    print(f"  One hour later: {one_hour_later.strftime('%H:%M:%S')}")
    print(f"  30 minutes ago: {thirty_minutes_ago.strftime('%H:%M:%S')}")
    print(
        f"  2 days 3 hours from now: {two_days_three_hours.strftime('%Y-%m-%d %H:%M')}"
    )
    print()

    # Date comparisons
    birthday = date(2024, 7, 15)
    new_years = date(2025, 1, 1)

    print("Date comparisons:")
    print(f"  Is birthday ({birthday}) after today? {birthday > today}")
    print(f"  Is New Year's ({new_years}) after birthday? {new_years > birthday}")
    print(
        f"  Is today between birthday and New Year's? {birthday <= today <= new_years}"
    )
    print()

    # Time differences
    start_time = datetime(2024, 1, 1, 9, 0, 0)
    end_time = datetime(2024, 1, 1, 17, 30, 0)
    time_diff = end_time - start_time

    print("Time differences:")
    print(f"  Start: {start_time.strftime('%H:%M')}")
    print(f"  End: {end_time.strftime('%H:%M')}")
    print(f"  Difference: {time_diff}")
    print(f"  Hours: {time_diff.total_seconds() / 3600:.2f}")
    print(f"  Minutes: {time_diff.total_seconds() / 60:.1f}")


def exercise_3_calendar_operations():
    """
    Calendar-related operations.

    1. Get month calendar
    2. Check leap years
    3. Get day of week
    4. Calculate business days
    """
    print("\n\nExercise 3: Calendar Operations")
    print("-" * 40)

    year = 2024
    month = 3  # March

    # Get month calendar
    cal = calendar.monthcalendar(year, month)

    print(f"Calendar for {calendar.month_name[month]} {year}:")
    print(" Mo Tu We Th Fr Sa Su")
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2d} "
        print(f" {week_str}")

    print()

    # Leap year check
    print("Leap year checks:")
    for y in [2020, 2021, 2024, 2100]:
        is_leap = calendar.isleap(y)
        print(f"  {y}: {'Leap year' if is_leap else 'Not leap year'}")

    print()

    # Day of week
    test_date = date(2024, 3, 15)  # March 15, 2024
    day_of_week = test_date.weekday()  # Monday=0, Sunday=6
    day_name = calendar.day_name[day_of_week]

    print(f"Day of week for {test_date}:")
    print(f"  Weekday number: {day_of_week} (0=Monday)")
    print(f"  Day name: {day_name}")

    # Business days calculation
    print("\nBusiness days calculation:")

    def count_business_days(start_date, end_date):
        """Count business days (Monday-Friday) between two dates."""
        business_days = 0
        current_date = start_date

        while current_date <= end_date:
            if current_date.weekday() < 5:  # Monday=0, Friday=4
                business_days += 1
            current_date += timedelta(days=1)

        return business_days

    start = date(2024, 3, 1)  # March 1, 2024 (Friday)
    end = date(2024, 3, 15)  # March 15, 2024 (Friday)

    total_days = (end - start).days + 1
    business_days = count_business_days(start, end)
    weekend_days = total_days - business_days

    print(f"  From {start} to {end}:")
    print(f"    Total days: {total_days}")
    print(f"    Business days: {business_days}")
    print(f"    Weekend days: {weekend_days}")


def exercise_4_timezones_conversions():
    """
    Timezone handling (conceptual - using UTC offsets).

    1. Work with UTC
    2. Convert between timezones (conceptually)
    3. Handle daylight saving time
    """
    print("\n\nExercise 4: Timezone Concepts")
    print("-" * 40)

    # Note: For actual timezone support, use pytz or zoneinfo (Python 3.9+)
    # This exercise uses UTC offsets for demonstration

    from datetime import timezone

    # UTC time
    utc_now = datetime.now(timezone.utc)
    print(f"Current UTC time: {utc_now}")

    # Create timezone-aware datetimes with offsets
    print("\nTimezones with UTC offsets:")

    # Eastern Time (UTC-5)
    eastern_offset = timedelta(hours=-5)
    eastern_time = utc_now + eastern_offset
    print(f"  Eastern Time (UTC-5): {eastern_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Pacific Time (UTC-8)
    pacific_offset = timedelta(hours=-8)
    pacific_time = utc_now + pacific_offset
    print(f"  Pacific Time (UTC-8): {pacific_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Central European Time (UTC+1)
    cet_offset = timedelta(hours=1)
    cet_time = utc_now + cet_offset
    print(f"  CET (UTC+1): {cet_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # India Standard Time (UTC+5:30)
    ist_offset = timedelta(hours=5, minutes=30)
    ist_time = utc_now + ist_offset
    print(f"  IST (UTC+5:30): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Timezone conversions
    print("\nTimezone conversions:")

    # Meeting at 2 PM Eastern
    meeting_eastern = datetime(2024, 3, 15, 14, 0, 0)  # March 15, 2 PM "Eastern"
    print(f"  Meeting in 'Eastern': {meeting_eastern.strftime('%Y-%m-%d %H:%M')}")

    # Convert to Pacific
    meeting_pacific = meeting_eastern + timedelta(hours=-3)  # EST to PST
    print(f"  Meeting in 'Pacific': {meeting_pacific.strftime('%Y-%m-%d %H:%M')}")

    # Convert to UTC
    meeting_utc = meeting_eastern + timedelta(hours=5)  # EST to UTC
    print(f"  Meeting in UTC: {meeting_utc.strftime('%Y-%m-%d %H:%M')}")

    # Daylight saving time considerations
    print("\nDaylight saving time note:")
    print("  DST typically adds 1 hour in spring, subtracts 1 hour in fall")
    print("  Always use timezone-aware datetimes for production code")
    print("  Consider using: from zoneinfo import ZoneInfo (Python 3.9+)")
    print("  Or: import pytz (for older Python versions)")


def exercise_5_date_validation_manipulation():
    """
    Date validation and manipulation.

    1. Validate dates
    2. Calculate age
    3. Find next occurrence of a date
    4. Date ranges and intervals
    """
    print("\n\nExercise 5: Date Validation & Manipulation")
    print("-" * 40)

    # Date validation
    def is_valid_date(year, month, day):
        """Check if a date is valid."""
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False

    test_dates = [
        (2024, 2, 29),  # Valid (leap year)
        (2023, 2, 29),  # Invalid
        (2024, 13, 1),  # Invalid month
        (2024, 12, 32),  # Invalid day
        (2024, 4, 31),  # Invalid (April has 30 days)
    ]

    print("Date validation:")
    for y, m, d in test_dates:
        valid = is_valid_date(y, m, d)
        print(f"  {y:04d}-{m:02d}-{d:02d}: {'✓ Valid' if valid else '✗ Invalid'}")

    print()

    # Calculate age
    def calculate_age(birth_date, reference_date=None):
        """Calculate age in years."""
        if reference_date is None:
            reference_date = date.today()

        age = reference_date.year - birth_date.year

        # Adjust if birthday hasn't occurred yet this year
        if (reference_date.month, reference_date.day) < (
            birth_date.month,
            birth_date.day,
        ):
            age -= 1

        return age

    birthdays = [
        date(1990, 7, 15),
        date(2000, 1, 1),
        date(1985, 12, 31),
    ]

    print("Age calculation (as of today):")
    for bday in birthdays:
        age = calculate_age(bday)
        print(f"  Born {bday}: {age} years old")

    print()

    # Find next occurrence
    def next_occurrence_of_date(target_month, target_day, reference_date=None):
        """Find the next occurrence of a month/day after reference date."""
        if reference_date is None:
            reference_date = date.today()

        # Try this year
        try:
            this_year = date(reference_date.year, target_month, target_day)
            if this_year > reference_date:
                return this_year
        except ValueError:
            pass  # Invalid date (e.g., Feb 29 in non-leap year)

        # Try next year
        next_year = reference_date.year + 1
        while True:
            try:
                return date(next_year, target_month, target_day)
            except ValueError:
                next_year += 1

    print("Next occurrence of dates:")
    today = date.today()

    events = [
        ("Christmas", 12, 25),
        ("Valentine's Day", 2, 14),
        ("Halloween", 10, 31),
        ("April Fools", 4, 1),
    ]

    for name, month, day in events:
        next_date = next_occurrence_of_date(month, day, today)
        days_until = (next_date - today).days
        print(f"  {name}: {next_date} (in {days_until} days)")

    print()

    # Date ranges
    print("Date ranges:")

    def generate_date_range(start_date, end_date):
        """Generate all dates in a range."""
        current = start_date
        while current <= end_date:
            yield current
            current += timedelta(days=1)

    start = date(2024, 3, 1)
    end = date(2024, 3, 7)

    print(f"  Dates from {start} to {end}:")
    for d in generate_date_range(start, end):
        print(f"    {d.strftime('%A, %b %d')}")


def mini_project_event_scheduler():
    """
    Event Scheduler

    A system to manage events with the following features:
    1. Add events with date, time, and duration
    2. View upcoming events
    3. Check for scheduling conflicts
    4. Send reminders for upcoming events
    5. Save and load events from file
    """
    print("\n" + "=" * 60)
    print("MINI PROJECT: EVENT SCHEDULER")
    print("=" * 60)

    events_file = "events.json"
    events = []

    class Event:
        def __init__(
            self, title, description, event_date, event_time, duration_hours=1
        ):
            self.title = title
            self.description = description
            self.event_date = event_date
            self.event_time = event_time
            self.duration_hours = duration_hours
            self.created_at = datetime.now()

            # Combine date and time
            self.start_datetime = datetime.combine(event_date, event_time)
            self.end_datetime = self.start_datetime + timedelta(hours=duration_hours)

        def to_dict(self):
            """Convert event to dictionary for JSON serialization."""
            return {
                "title": self.title,
                "description": self.description,
                "event_date": self.event_date.isoformat(),
                "event_time": self.event_time.isoformat(),
                "duration_hours": self.duration_hours,
                "created_at": self.created_at.isoformat(),
            }

        @classmethod
        def from_dict(cls, data):
            """Create event from dictionary."""
            event_date = date.fromisoformat(data["event_date"])
            event_time = time.fromisoformat(data["event_time"])
            created_at = datetime.fromisoformat(data["created_at"])

            event = cls(
                title=data["title"],
                description=data["description"],
                event_date=event_date,
                event_time=event_time,
                duration_hours=data["duration_hours"],
            )
            event.created_at = created_at
            return event

        def __str__(self):
            return (
                f"{self.title}: {self.event_date.strftime('%A, %b %d, %Y')} "
                f"at {self.event_time.strftime('%I:%M %p')} "
                f"({self.duration_hours} hour{'s' if self.duration_hours != 1 else ''})"
            )

    def load_events():
        """Load events from file."""
        nonlocal events
        if os.path.exists(events_file):
            try:
                with open(events_file, "r") as f:
                    data = json.load(f)
                    events = [Event.from_dict(item) for item in data]
                print(f"Loaded {len(events)} events from {events_file}")
            except Exception as e:
                print(f"Error loading events: {e}")
                events = []
        else:
            events = []

    def save_events():
        """Save events to file."""
        try:
            data = [event.to_dict() for event in events]
            with open(events_file, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Saved {len(events)} events to {events_file}")
        except Exception as e:
            print(f"Error saving events: {e}")

    def add_event():
        """Add a new event."""
        print("\n--- Add New Event ---")

        title = input("Event title: ")
        description = input("Description: ")

        # Get date
        while True:
            date_str = input("Event date (YYYY-MM-DD): ")
            try:
                event_date = date.fromisoformat(date_str)
                break
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        # Get time
        while True:
            time_str = input("Event time (HH:MM): ")
            try:
                hour, minute = map(int, time_str.split(":"))
                event_time = time(hour, minute)
                break
            except ValueError, TypeError:
                print("Invalid time format. Use HH:MM.")

        # Get duration
        while True:
            duration_str = input("Duration in hours (default: 1): ")
            if not duration_str:
                duration_hours = 1
                break
            try:
                duration_hours = float(duration_str)
                if duration_hours > 0:
                    break
                else:
                    print("Duration must be positive.")
            except ValueError:
                print("Invalid duration.")

        # Create event
        event = Event(title, description, event_date, event_time, duration_hours)

        # Check for conflicts
        conflicts = check_conflicts(event)
        if conflicts:
            print(f"\n⚠️  Scheduling conflicts found:")
            for conflict in conflicts:
                print(
                    f"  - {conflict.title} at {conflict.event_time.strftime('%I:%M %p')}"
                )

            confirm = input("Add event anyway? (y/n): ")
            if confirm.lower() != "y":
                print("Event cancelled.")
                return

        events.append(event)
        save_events()
        print(f"\n✅ Event added: {event}")

    def check_conflicts(new_event):
        """Check if new event conflicts with existing events."""
        conflicts = []
        for existing_event in events:
            if existing_event.event_date == new_event.event_date:
                # Check for time overlap
                if not (
                    new_event.end_datetime <= existing_event.start_datetime
                    or new_event.start_datetime >= existing_event.end_datetime
                ):
                    conflicts.append(existing_event)
        return conflicts

    def view_events():
        """View all events."""
        if not events:
            print("\nNo events scheduled.")
            return

        print(f"\n--- All Events ({len(events)}) ---")

        # Sort events by date and time
        sorted_events = sorted(events, key=lambda e: e.start_datetime)

        for i, event in enumerate(sorted_events, 1):
            print(f"\n{i}. {event}")
            print(f"   Description: {event.description}")
            print(f"   Created: {event.created_at.strftime('%Y-%m-%d %H:%M')}")

    def view_upcoming_events(days_ahead=7):
        """View events in the next specified number of days."""
        today = date.today()
        cutoff_date = today + timedelta(days=days_ahead)

        upcoming = [e for e in events if today <= e.event_date <= cutoff_date]

        if not upcoming:
            print(f"\nNo events in the next {days_ahead} days.")
            return

        print(f"\n--- Upcoming Events (next {days_ahead} days) ---")

        # Group by date
        events_by_date = {}
        for event in upcoming:
            if event.event_date not in events_by_date:
                events_by_date[event.event_date] = []
            events_by_date[event.event_date].append(event)

        # Sort dates
        sorted_dates = sorted(events_by_date.keys())

        for event_date in sorted_dates:
            print(f"\n{event_date.strftime('%A, %b %d, %Y')}:")
            day_events = sorted(events_by_date[event_date], key=lambda e: e.event_time)

            for event in day_events:
                days_until = (event.event_date - today).days
                day_str = (
                    "Today"
                    if days_until == 0
                    else f"In {days_until} day{'s' if days_until != 1 else ''}"
                )
                print(
                    f"  • {event.event_time.strftime('%I:%M %p')}: {event.title} ({day_str})"
                )

    def send_reminders():
        """Show reminders for events happening soon."""
        now = datetime.now()
        cutoff = now + timedelta(hours=24)  # Next 24 hours

        reminders = []
        for event in events:
            if now <= event.start_datetime <= cutoff:
                time_until = event.start_datetime - now
                hours = int(time_until.total_seconds() // 3600)
                minutes = int((time_until.total_seconds() % 3600) // 60)

                reminders.append((event, hours, minutes))

        if not reminders:
            print("\nNo events in the next 24 hours.")
            return

        print("\n--- Reminders (next 24 hours) ---")
        for event, hours, minutes in reminders:
            if hours > 0:
                time_str = f"{hours} hour{'s' if hours != 1 else ''} {minutes} minute{'s' if minutes != 1 else ''}"
            else:
                time_str = f"{minutes} minute{'s' if minutes != 1 else ''}"

            print(f"\n⚠️  {event.title} starts in {time_str}")
            print(f"   Time: {event.event_time.strftime('%I:%M %p')}")
            print(f"   Description: {event.description}")

    def delete_event():
        """Delete an event."""
        if not events:
            print("\nNo events to delete.")
            return

        view_events()

        try:
            choice = int(input("\nEnter event number to delete (0 to cancel): "))
            if choice == 0:
                return

            if 1 <= choice <= len(events):
                event = events[choice - 1]
                confirm = input(f"Delete '{event.title}'? (y/n): ")
                if confirm.lower() == "y":
                    events.pop(choice - 1)
                    save_events()
                    print("Event deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid event number.")
        except ValueError:
            print("Invalid input.")

    # Load events at startup
    load_events()

    while True:
        print("\n" + "-" * 60)
        print("EVENT SCHEDULER")
        print("-" * 60)
        print("1. Add new event")
        print("2. View all events")
        print("3. View upcoming events (next 7 days)")
        print("4. Check reminders (next 24 hours)")
        print("5. Delete event")
        print("6. Exit")
        print("-" * 60)

        choice = input("Select option (1-6): ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            view_upcoming_events()
        elif choice == "4":
            send_reminders()
        elif choice == "5":
            delete_event()
        elif choice == "6":
            print("\nSaving events and exiting...")
            save_events()

            # Clean up test file if empty
            if not events and os.path.exists(events_file):
                os.remove(events_file)

            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def run_all_exercises():
    """Run all Day 24 exercises."""
    print("=" * 60)
    print("Week 4, Day 24: Dates & Times")
    print("=" * 60)

    print("\nThis day covers working with dates, times, timezones,")
    print("and calendar operations.")
    print("\nRunning exercises...")

    exercise_1_datetime_basics()
    exercise_2_date_arithmetic()
    exercise_3_calendar_operations()
    exercise_4_timezones_conversions()
    exercise_5_date_validation_manipulation()

    print("\n" + "=" * 60)
    print("Mini Project: Event Scheduler")
    print("=" * 60)
    mini_project_event_scheduler()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 24 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
