from solution import life_period
import unittest

class TestLifePeriod(unittest.TestCase):

  message = "Wrong result for case "

  def test_1_invalid_case(self):
    expected = "INVALID"
    self.assertEqual(life_period(0), expected, self.message + expected)

  def test_2_child_case(self):
    expected = "CHILD"
    self.assertEqual(life_period(1), expected, self.message + expected)
    self.assertEqual(life_period(15), expected, self.message + expected)

  def test_3_adult_case(self):
    expected = "ADULT"
    self.assertEqual(life_period(16), expected, self.message + expected)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)