import unittest
import sys
import os


# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from .solution import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "anagram", t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))
    
    def test_example_2(self):
        s = "rat", t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))

if __name__ == '__main__':
    unittest.main()
