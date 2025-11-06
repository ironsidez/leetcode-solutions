import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # nums = [-1,0,1,2,-1,-4]
        # Expected: [[-1,-1,2],[-1,0,1]]
        pass
    
    def test_example_2(self):
        # nums = [0,1,1]
        # Expected: []
        pass

if __name__ == '__main__':
    unittest.main()
