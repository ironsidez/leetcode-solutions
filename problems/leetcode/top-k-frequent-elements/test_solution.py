import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from .solution import Solution

class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [4,4,2,1,1,1,2,2,3,4,4,2]
        k = 2
        result = self.solution.topKFrequent(nums, k)
        expected = [4,2]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        nums = [1]
        k = 1
        result = self.solution.topKFrequent(nums, k)
        expected = [1]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
