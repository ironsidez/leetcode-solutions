import unittest
from typing import List
from .solution import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        expected = [0, 1]
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        result = self.solution.twoSum(nums, target)
        expected = [1, 2]
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        expected = [0, 1]
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = self.solution.twoSum(nums, target)
        expected = [2, 4]
        self.assertEqual(result, expected)
    
    def test_mixed_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        result = self.solution.twoSum(nums, target)
        expected = [0, 2]
        self.assertEqual(result, expected)
    
    def test_large_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 19
        result = self.solution.twoSum(nums, target)
        expected = [8, 9]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
