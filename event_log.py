from datetime import datetime
from storage import load_events, save_events


def log_event(username, habit_name, action):
    events = load_events()

    events.append({
        "username": username,
        "habit_name": habit_name,
        "action": action,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_events(events)


def get_user_events(username):
    events = load_events()
    return [event for event in events if event["username"] == username]