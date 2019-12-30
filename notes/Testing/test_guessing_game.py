import unittest
import testing_python

# run this file using command: `python3 test_guessing_game.py`

class TestGame(unittest.TestCase):
    def test_input(self):
        result = testing_python.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = testing_python.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = testing_python.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = testing_python.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

# run this file using command: `python3 test_guessing_game.py`

# ===========================================================================