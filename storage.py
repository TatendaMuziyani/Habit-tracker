"""
This file saves and loads data.
"""

import json
import os
from habit import Habit

DATA_DIR = "data"
HABITS_FILE = os.path.join(DATA_DIR, "habits.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")


def ensure_data_files():
    """Create the data files if they do not exist."""
    os.makedirs(DATA_DIR, exist_ok=True)

    for file_path in [HABITS_FILE, USERS_FILE, EVENTS_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)


def load_habits():
    """Load all saved habits."""
    ensure_data_files()
    try:
        with open(HABITS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []

    return [Habit.from_dict(item) for item in data]


def save_habits(habits):
    """Save all habits."""
    ensure_data_files()
    data = [habit.to_dict() for habit in habits]

    with open(HABITS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_users():
    """Load all saved users."""
    ensure_data_files()
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_users(users):
    """Save all users."""
    ensure_data_files()
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def load_events():
    """Load all saved events."""
    ensure_data_files()
    try:
        with open(EVENTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_events(events):
    """Save all events."""
    ensure_data_files()
    with open(EVENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)