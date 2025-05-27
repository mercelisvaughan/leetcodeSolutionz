from typing import List

"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

cut the list in half -> middle_index = len(nums) // 2
have two pointers, one at the start and one at the end
loop through the loop logically 
nums[middle_index] is the number we're constantly keep track of 

middle_index = len(nums) // 2
"""

def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0 # starting pointer
    end = len(nums) - 1 # ending pointer
    while start <= end: # loop through the array and move our pointers
        middle_index = (start + end) // 2 # the middle is the start + end divided by 2
        if nums[middle_index] == target: # if middle == target we found it
            return middle_index
        elif nums[middle_index] < target: # if middle is less than target than the target is in the right side of the array
            start = middle_index + 1 
            # now our new start is the index to the right of the middle since 
            # its on the right side and we dont move the end pointer
            # we dont increment the end pointer because we dont need to
        else:
            end = middle_index - 1
            # if all else fails, then we move the end pointer to the left of the middle
            # (cutting the list in half)
    return start # if we dont find it this has to be the only one
