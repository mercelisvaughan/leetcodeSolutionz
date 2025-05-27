from typing import List

class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        # if strings is empty return empty string
        if not strings:
            return ""
        

        initial_string = strings[0] # this is the first word
        for string in strings[1:]:
            while not string.startswith(initial_string):
                initial_string = initial_string[:-1]
                if not initial_string: # if the initial string becomes empty
                    return ""

        return initial_string
    
"""
To solve thisproblem we basically take the initial string (the first string in the array) and compare
it to the rest of the strings, shortening it along the way from the back
"""

c = Solution()
print("answer: --------------------------------------- ")
print(c.longestCommonPrefix(["flower","flow","flight"]))
print("answer: --------------------------------------- ")
print(c.longestCommonPrefix(["dog","racecar","car"]))