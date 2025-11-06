from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in numMap:
                return [numMap[complement], index]
            numMap[value] = index

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(f"Result: {result}")  # Should print [0, 1]

