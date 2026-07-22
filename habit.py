"""
This file creates the Habit class.
"""

from datetime import datetime


class Habit:
    """Create a habit and keep its information."""

    def __init__(self, name, period="Daily", owner="default", created_at=None, completed_dates=None):
        """Set up a new habit."""
        self.name = name.strip()
        self.period = period.strip().title()
        self.owner = owner.strip()
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d")
        self.completed_dates = completed_dates or []

    def complete_habit(self):
        """Mark the habit as completed for today."""
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.completed_dates:
            self.completed_dates.append(today)
            self.completed_dates.sort()
            return True
        return False

    def current_streak(self):
        """Return the current streak for the habit."""
        if not self.completed_dates:
            return 0

        dates = sorted(set(self.completed_dates))
        streak = 1

        for i in range(len(dates) - 1, 0, -1):
            current_day = datetime.strptime(dates[i], "%Y-%m-%d").date()
            previous_day = datetime.strptime(dates[i - 1], "%Y-%m-%d").date()

            if (current_day - previous_day).days == 1:
                streak += 1
            else:
                break

        return streak

    def to_dict(self):
        """Change the habit into a dictionary."""
        return {
            "name": self.name,
            "period": self.period,
            "owner": self.owner,
            "created_at": self.created_at,
            "completed_dates": self.completed_dates
        }

    @classmethod
    def from_dict(cls, data):
        """Create a habit from saved data."""
        return cls(
            name=data.get("name", ""),
            period=data.get("period", "Daily"),
            owner=data.get("owner", "default"),
            created_at=data.get("created_at"),
            completed_dates=data.get("completed_dates", [])
        )