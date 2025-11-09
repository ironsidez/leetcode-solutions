import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from .solution import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [1,2,3,4]
        result = self.solution.productExceptSelf(nums)
        expected = [24,12,8,6]
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [-1,1,0,-3,3]
        result = self.solution.productExceptSelf(nums)
        expected = [0,0,9,0,0]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
