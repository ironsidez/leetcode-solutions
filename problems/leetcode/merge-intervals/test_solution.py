import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # intervals = [[1,3],[2,6],[8,10],[15,18]]
        # Expected: [[1,6],[8,10],[15,18]]
        pass
    
    def test_example_2(self):
        # intervals = [[1,4],[4,5]]
        # Expected: [[1,5]]
        pass

if __name__ == '__main__':
    unittest.main()
