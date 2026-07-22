import unittest
from habit import Habit
from analytics import current_streak, longest_streak, completion_percentage


class TestAnalytics(unittest.TestCase):
    def test_current_streak(self):
        habit = Habit("Exercise")
        habit.completed_dates = ["2026-07-17", "2026-07-18", "2026-07-19"]
        self.assertEqual(current_streak(habit), 3)

    def test_longest_streak(self):
        habit = Habit("Exercise")
        habit.completed_dates = ["2026-07-10", "2026-07-11", "2026-07-13", "2026-07-14", "2026-07-15"]
        self.assertEqual(longest_streak(habit), 3)

    def test_completion_percentage(self):
        habit = Habit("Exercise", created_at="2026-07-17")
        habit.completed_dates = ["2026-07-17", "2026-07-18"]
        result = completion_percentage(habit)
        self.assertTrue(result >= 0)


if __name__ == "__main__":
    unittest.main()