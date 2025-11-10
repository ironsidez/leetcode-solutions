from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        previousNum = sortedNums[0] if sortedNums else None
        longestSequenceLen = 1
        currentSequenceLen = 1

        for num in sortedNums:
            if num == previousNum + 1:
                currentSequenceLen += 1
                if currentSequenceLen > longestSequenceLen:
                    longestSequenceLen = currentSequenceLen
            elif num != previousNum:
                currentSequenceLen = 1
                    
            previousNum = num
        return longestSequenceLen