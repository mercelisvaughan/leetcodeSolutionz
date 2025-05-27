from typing import List

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space. aka no extra data structures

This is a 2 pointer solution, what we will do is ask if the sum is
less than or greater than the sum and move our pointers depending on which condiion is true
we use a while loop because we dont know many times we are going to iterate

"""

numbers = [2,7,11,15]


def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        print("l: ", l)
        print("r: ", r)
        print("----------------")
        print("sum= ", numbers[l] + numbers[r])
        if numbers[l] + numbers[r] > target:
            r-=1
        elif numbers[l] + numbers[r] < target:
            l+=1
        else:
            return [l+1, r+1]
        
print(twoSum(numbers, target=9))