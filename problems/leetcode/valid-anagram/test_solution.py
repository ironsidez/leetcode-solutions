import unittest
import sys
import os


# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # s = "anagram", t = "nagaram"
        # Expected: True
        pass
    
    def test_example_2(self):
        # s = "rat", t = "car"
        # Expected: False
        pass

if __name__ == '__main__':
    unittest.main()
