from typing import List

def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)-1):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 2))