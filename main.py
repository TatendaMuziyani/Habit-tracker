"""
This file runs the Habit Tracker.
"""

from habit import Habit
from storage import load_habits, save_habits, ensure_data_files
from auth import login_or_register
from event_log import log_event
from analytics import (
    current_streak,
    longest_streak,
    completion_percentage,
    habit_statistics,
    filter_habits_by_frequency
)


def get_user_habits(habits, username):
    """Get the habits for the current user."""
    return [habit for habit in habits if habit.owner == username]


def display_menu():
    """Show the main menu."""
    print("\n========== HABIT TRACKER ==========")
    print("1. Create Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Delete Habit")
    print("5. Analytics")
    print("6. Filter Habits by Frequency")
    print("7. Logout / Exit")


def show_habits(habits):
    """Show all the habits."""
    if not habits:
        print("No habits found.")
        return

    for index, habit in enumerate(habits, start=1):
        print(f"{index}. {habit.name} | {habit.period} | Created: {habit.created_at} | Completed Days: {len(habit.completed_dates)}")


def main():
    """Run the Habit Tracker."""
    ensure_data_files()
    username = login_or_register()

    if not username:
        print("Goodbye!")
        return

    all_habits = load_habits()

    while True:
        user_habits = get_user_habits(all_habits, username)
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter habit name: ").strip()
            period = input("Enter period (Daily/Weekly/Monthly): ").strip()

            habit = Habit(name=name, period=period, owner=username)
            all_habits.append(habit)
            save_habits(all_habits)

            print("Habit created successfully.")

        elif choice == "2":
            print("\nYour Habits:")
            show_habits(user_habits)

        elif choice == "3":
            if not user_habits:
                print("No habits to complete.")
                continue

            print("\nYour Habits:")
            show_habits(user_habits)

            try:
                number = int(input("Choose habit number: ")) - 1
                selected_habit = user_habits[number]
            except (ValueError, IndexError):
                print("Invalid choice.")
                continue

            if selected_habit.complete_habit():
                save_habits(all_habits)
                log_event(username, selected_habit.name, "completed")
                print("Habit marked as completed.")
            else:
                print("This habit is already completed today.")

        elif choice == "4":
            if not user_habits:
                print("No habits to delete.")
                continue

            print("\nYour Habits:")
            show_habits(user_habits)

            try:
                number = int(input("Choose habit number to delete: ")) - 1
                selected_habit = user_habits[number]
            except (ValueError, IndexError):
                print("Invalid choice.")
                continue

            all_habits.remove(selected_habit)
            save_habits(all_habits)
            log_event(username, selected_habit.name, "deleted")
            print("Habit deleted successfully.")

        elif choice == "5":
            if not user_habits:
                print("No habits available for analytics.")
                continue

            stats = habit_statistics(user_habits)
            print("\n========== ANALYTICS ==========")
            print(f"Total habits: {stats['total_habits']}")
            print(f"Total completed events: {stats['total_completed_events']}")
            print(f"Completed habits: {stats['completed_habits_count']}")
            print(f"Most completed habit: {stats['most_completed']}")
            print(f"Least completed habit: {stats['least_completed']}")

            for habit in user_habits:
                print("\n--------------------")
                print(f"Habit: {habit.name}")
                print(f"Current streak: {current_streak(habit)}")
                print(f"Longest streak: {longest_streak(habit)}")
                print(f"Completion percentage: {completion_percentage(habit)}%")

        elif choice == "6":
            freq = input("Enter frequency to filter by (Daily/Weekly/Monthly): ").strip()
            filtered = filter_habits_by_frequency(user_habits, freq)

            print("\nFiltered Habits:")
            show_habits(filtered)

        elif choice == "7":
            print("Logging out. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()