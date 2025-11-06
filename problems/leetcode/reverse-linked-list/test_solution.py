import unittest
import sys
import os
from typing import Optional

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        # head = [1,2,3,4,5]
        # Expected: [5,4,3,2,1]
        pass
    
    def test_example_2(self):
        # head = [1,2]
        # Expected: [2,1]
        pass

if __name__ == '__main__':
    unittest.main()
