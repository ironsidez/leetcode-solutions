import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [100,4,200,1,3,2]
        result = self.solution.longestConsecutive(nums)
        expected = 4
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        result = self.solution.longestConsecutive(nums)
        expected = 9
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
