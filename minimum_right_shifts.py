from typing import List
"""

2855. Minimum Right Shifts to Sort the Array

You are given a 0-indexed array nums of length n containing distinct positive integers.
Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.

"""

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
    # A circularly sorted array is one where after some rotations
    # the array becomes sorted in ascending order.
    # Check if the array is sorted after every right shift.
    # Return the count of shifts required; if it's not possible, return -1.



        n = len(nums)
        k %= n  # Handle cases where k > n
        nums[-k:] + nums[:-k]
        counter = 0
        #
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                nums[-k:] + nums[:-k]
                counter += 1

        return counter

        



        #

        #
        return None
    

def shift_right(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]
