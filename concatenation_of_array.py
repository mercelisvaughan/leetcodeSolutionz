from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * (2 * n)

        for i in nums:
            answer[i] = nums[i]
            
        return answer

nums = [1,2,1]
print(getConcatenation(nums))