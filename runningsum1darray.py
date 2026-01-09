from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0 # sets the count to zero
        for i in nums:
            runningSum += nums[i]
            nums[i] = runningSum
        return nums
    
    def prodOfArray(self, nums: List[int]) -> List[int]:
        
        



        return nums
    
