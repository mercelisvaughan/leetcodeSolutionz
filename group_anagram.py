from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # {'', []}
        for word in strs:
            signature = "".join(sorted(word))
            anagram_map[signature].append(word)
        return anagram_map
    

strs = ["act","pots","tops","cat","stop","hat"]
s = Solution()
print(s.groupAnagrams(strs))