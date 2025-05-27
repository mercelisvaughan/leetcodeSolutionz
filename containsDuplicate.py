from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett = set()

        for number in nums:
            if number in sett:
                return True
            sett.add(nums[number])
        return False
    
c = Solution()

print(c.containsDuplicate([1,2,3,4]))