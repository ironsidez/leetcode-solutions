from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for number in nums:
            if number in frequencyMap:
                frequencyMap[number] += 1
            else:
                frequencyMap[number] = 1

        sortedMap = sorted(frequencyMap.items(), key=lambda x: x[1], reverse=True)
        topK = sortedMap[:k]
        return [item[0] for item in topK]
            

