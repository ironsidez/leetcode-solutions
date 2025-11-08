import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from .solution import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = self.solution.groupAnagrams(strs)
        
        # Convert result to sets of frozensets for comparison (order doesn't matter)
        result_sets = {frozenset(group) for group in result}
        expected_sets = {
            frozenset(["eat", "tea", "ate"]),
            frozenset(["tan", "nat"]),
            frozenset(["bat"])
        }
        
        self.assertEqual(result_sets, expected_sets)
    
    def test_example_2(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
