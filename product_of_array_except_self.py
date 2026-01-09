"""

Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

keep one pointer on lst[i]
iterate other pointer to touch every index except lst[i]




"""

from typing import List

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # prefix pass
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # suffix pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


arr = [1,2,3,4,5]
c = Solution()
print(c.productExceptSelf(arr))