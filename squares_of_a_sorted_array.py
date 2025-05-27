from typing import List

"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 2 pointer approach

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""

"""

Answer: Loop through the array and square every number in place, place Left pointer at the front of the list
Place Right pointer at nums[-1] then place number in proper position

"""
nums = [-7,-3,2,3,11]

print(len(nums)-1)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1
        result = [0] * len(nums) # create a new list with the same length as nums but filled with zeros

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = (nums[left]**2)
                left += 1
            else:
                result[pos] = (nums[right]**2)
                right -= 1
            pos -= 1

        return result.reverse()