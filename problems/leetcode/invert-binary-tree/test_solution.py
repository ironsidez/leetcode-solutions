import unittest
import sys
import os
from typing import Optional

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # root = [4,2,7,1,3,6,9]
        # Expected: [4,7,2,9,6,3,1]
        pass
    
    def test_example_2(self):
        # root = [2,1,3]
        # Expected: [2,3,1]
        pass

if __name__ == '__main__':
    unittest.main()
