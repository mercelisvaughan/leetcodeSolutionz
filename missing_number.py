from typing import List

"""
TODO
look up how to use the enumerate function
This specific problem is not a typical two-pointer problem.
A two-pointer technique usually involves iterating over two parts of an array
simultaneously,
typically when working with sorted arrays, intervals, or finding pairs/triplets.

For finding the missing number, sorting the array and using two
indices (start and faster) doesn't logically apply, as the problem
is about finding a single missing value in a range of numbers.
Key Observations for Missing Number Problem

    The numbers are in the range [0, n], where n is the length of the array.
    Exactly one number is missing.
    Sorting isn't required for this problem — there are more efficient approaches.

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        return None
    

nums = [9,6,4,2,3,5,7,0,1]
c = Solution()
print(c.missingNumber(nums))