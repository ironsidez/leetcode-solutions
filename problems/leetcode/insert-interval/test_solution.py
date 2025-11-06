import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # intervals = [[1,3],[6,9]], newInterval = [2,5]
        # Expected: [[1,5],[6,9]]
        pass
    
    def test_example_2(self):
        # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        # Expected: [[1,2],[3,10],[12,16]]
        pass

if __name__ == '__main__':
    unittest.main()
