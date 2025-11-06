import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # height = [1,8,6,2,5,4,8,3,7]
        # Expected: 49
        pass
    
    def test_example_2(self):
        # height = [1,1]
        # Expected: 1
        pass

if __name__ == '__main__':
    unittest.main()
