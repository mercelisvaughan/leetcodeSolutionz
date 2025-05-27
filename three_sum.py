from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

How do we know this is a two pointer solution?
- We have to look at other numbers depending on the current sum
For example, if 
i + j + k > 0
one of our values has to be too big and we must move down the list to get a smaller number
vice versa if the number is too small

Solution
- Use two pointer to traverse the list inwards from end to end
we sort the list because we want to look at other numbers depending on the current sum
so our list looks like
[-1, -1, 0, 1, 2]

-1                                     2
we start here                  and we start here
we look at three numbers all at the same time
we 

"""

def threeSum(nums: List[int]) -> List[List[int]]:
    length_ofList = len(nums)
    nums.sort()

    result = []

    l = 2
    r = len(nums) - 1
    
    for i in range(length_ofList-2):
        a = nums[i]

        while l < r:
            if a + nums[l] + nums[r] == 0:
                result.append([a, nums[l], nums[r]])
                print("we found a triplet, we added tthem to the result list the trio is: ", a, nums[l], nums[r])
            elif a + nums[l] + nums[r] > 0:
                r -= 1
                print("we did not find a triplet because the sum of the three numbers was too large, we decrement r: ", nums[r])
            elif a + nums[l] + nums[r] < 0:
                l += 1
    return result

lst = [-1,0,1,2,-1,-4]
# -4, -1, -1, 0, 1, 2
print(threeSum(lst))
