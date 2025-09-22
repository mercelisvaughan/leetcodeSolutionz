from typing import List

"""

The idea is to add all of the elements to the hashmap,
the keys will be the elements,
and the value will
be the amount of times we see each key
then at the end we will sort the list
and return the k most elements from 0-k
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        answer = []
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        


        return answer

    

s = Solution()
nums = [1,2,2, 2,3,3,3, 3, 4]
k = 2
print(s.topKFrequent(nums, k))