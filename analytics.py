"""
Functions to analyze habit data.
"""

from datetime import datetime, date
from functools import reduce


def _parse_dates(habit):
    """It convert completed dates into sorted date objects."""
    return sorted(set(datetime.strptime(d, "%Y-%m-%d").date() for d in habit.completed_dates))


def current_streak(habit):
    """This will return the current streak for a habit."""
    dates = _parse_dates(habit)
    if not dates:
        return 0

    streak = 1
    for i in range(len(dates) - 1, 0, -1):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
        else:
            break
    return streak


def longest_streak(habit):
    """ The longest streak for a habit will be returned."""
    dates = _parse_dates(habit)
    if not dates:
        return 0

    longest = 1
    streak = 1

    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
        else:
            streak = 1

        if streak > longest:
            longest = streak

    return longest


def completion_percentage(habit):
    """Returns the completion percentage for a habit."""
    try:
        created_date = datetime.strptime(habit.created_at, "%Y-%m-%d").date()
    except ValueError:
        return 0.0

    today = date.today()
    days_active = (today - created_date).days + 1

    if days_active <= 0:
        return 0.0

    completed_days = len(set(habit.completed_dates))
    percentage = (completed_days / days_active) * 100
    return round(percentage, 2)


def filter_habits_by_frequency(habits, frequency):
    """It will return habits that match the given frequency."""
    return list(filter(lambda habit: habit.period.lower() == frequency.lower(), habits))


def habit_statistics(habits):
    """Return overall statistics for all habits."""
    total_habits = len(habits)
    total_completed = reduce(
        lambda total, habit: total + len(set(habit.completed_dates)),
        habits,
        0
    )

    names = list(map(lambda habit: habit.name, habits))
    completed_habits = list(filter(lambda habit: len(habit.completed_dates) > 0, habits))

    most_completed = None
    least_completed = None

    if habits:
        most_completed = max(habits, key=lambda habit: len(habit.completed_dates)).name
        least_completed = min(habits, key=lambda habit: len(habit.completed_dates)).name

    return {
        "total_habits": total_habits,
        "total_completed_events": total_completed,
        "habit_names": names,
        "completed_habits_count": len(completed_habits),
        "most_completed": most_completed,
        "least_completed": least_completed
    }