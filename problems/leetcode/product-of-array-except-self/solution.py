from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preproduct = 1
        postproduct =1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] *= preproduct  
            preproduct *= nums[i]
            result[-1 - i] *= postproduct
            postproduct *= nums[-1 - i]
        
        return result
