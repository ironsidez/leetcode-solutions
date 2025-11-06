import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        result = self.solution.search(nums, target)
        expected = 4
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        result = self.solution.search(nums, target)
        expected = -1
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
