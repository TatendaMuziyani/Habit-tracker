import unittest
from habit import Habit


class TestHabit(unittest.TestCase):
    def test_create_habit(self):
        habit = Habit("Exercise", "Daily", "tatenda")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.period, "Daily")
        self.assertEqual(habit.owner, "tatenda")

    def test_complete_habit(self):
        habit = Habit("Exercise")
        result = habit.complete_habit()
        self.assertTrue(result)
        self.assertEqual(len(habit.completed_dates), 1)

    def test_to_dict(self):
        habit = Habit("Exercise", "Daily", "tatenda")
        data = habit.to_dict()
        self.assertEqual(data["name"], "Exercise")
        self.assertEqual(data["owner"], "tatenda")


if __name__ == "__main__":
    unittest.main()