# This is an unittest file for the string_reversal.py!
# Never runs in production - just for development to check if all works fine
# I'm using unittest, but also can be used pytest - some courses in linkedin

import unittest
import string_reversal

class TestMain(unittest.TestCase):

    def setUp(self):
        print('TESTING CASE')

    def test_rev_loop(self):
        '''Testing the reverse loop with hello'''
        s = "hello"
        reversed_s = string_reversal.rev_loop(s)
        self.assertEqual(reversed_s,"olleh")

    def test_rev_loop2(self):
        s = "apple"
        reversed_s = string_reversal.rev_loop(s)
        self.assertEqual(reversed_s,"elppa")

    def tearDown(self):  # for more complicated tests
        print("CLEANING UP")

# to make sure that this is the main file that can be ran - use the __name__ - in that way we are sure that it will run only the test
# in this way we can run multiple test files in the same module at once - python -m unittest (-v = verbose)
if __name__ == "__main__":
    # this is just the main function of the unittest module - just run all the tests in the file
    unittest.main() 
