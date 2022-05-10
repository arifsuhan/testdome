from solution import deposit_interest
import unittest

class TestDepositeInterest(unittest.TestCase):

  message = "Wrong result for case "

  def test_1_unavailable(self):
    expected = "Unavailable"
    # optimal
    self.assertEqual(deposit_interest(100,17), expected, self.message + expected)
    self.assertEqual(deposit_interest(99,18), expected, self.message + expected)
    self.assertEqual(deposit_interest(10001,18), expected, self.message + expected)


  def test_2_interest_one_percent(self):
    expected = 1
    # optimal
    self.assertEqual(deposit_interest(100,18), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(999,18), expected, self.message + str(expected))
    # others
    self.assertEqual(deposit_interest(100,59), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(999,59), expected, self.message + str(expected))


  def test_3_interest_one_three_percent(self):
    expected = 1.3
    # optimal
    self.assertEqual(deposit_interest(1000,18), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(4999,59), expected, self.message + str(expected))
    # others
    self.assertEqual(deposit_interest(4999,18), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(1000,59), expected, self.message + str(expected))


  def test_4_interest_one_five_percent(self):
    expected = 1.5
    # optimal
    self.assertEqual(deposit_interest(5000,18), expected, self.message + str(expected))
    # others
    self.assertEqual(deposit_interest(5000,59), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(10000,18), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(10000,59), expected, self.message + str(expected))

  def test_5_interest_two_percent(self):
    expected = 2.0
    # optimal
    self.assertEqual(deposit_interest(10000,60), expected, self.message + str(expected))
    # others
    self.assertEqual(deposit_interest(100,60), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(999,60), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(4999,60), expected, self.message + str(expected))
    self.assertEqual(deposit_interest(5000,60), expected, self.message + str(expected))
    

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)