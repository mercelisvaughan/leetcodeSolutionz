"""
1. String Reduction (Minimum Length)
Difficulty: Medium | Topics: Stack

Problem Statement
You are given a string seq consisting only of the characters 'A' and 'B'. You may repeatedly perform the following operation:
Delete any occurrence of the substring "AB" or "BB".
After a deletion, the remaining parts of the string are concatenated.
Your task is to determine the minimum possible length of the string after performing any number of valid deletions.

Examples

Example 1:
Input: seq = "BABBA"
Output: 1
Explanation: 1. Delete "AB" at index 1: "BABBA" → "BBA". 2. Delete "BB" at index 0: "BBA" → "A". 3. No more moves. Length is 1.

Example 2:
Input: seq = "AB"
Output: 0
Explanation: Delete "AB". Length is 0.

Constraints
seq consists only of characters 'A' and 'B'.

Step-by-Step Solution

Initialize: Start with an empty list to act as your stack.
Iterate: Loop through each character in the sequence.
Peek & Compare: Look at the top of the stack (the last character added) using the index [-1].
If the pair formed by the top and the current character is "AB" or "BB", pop the top character and move to the next one.
Otherwise, push the current character onto the stack.
Result: The final length of the stack is your answer.

"""

def string_reduction(s: str) -> int:
    stack = []
    for character in s:
        if stack:
            c = stack[-1]
            if (c == 'A' and character == 'B' or c == 'B' and character =='B'):
                stack.pop()
                continue
        stack.append(character)
    return len(stack)


"""
s = 'BABBA'
stack = []
character = 'B'

c = stack[-1] = 'B'
# first iteration
-------------------
stack = ['B']
character = 'A'

c = stack[-1] = 'B'
character = 'A'

stack['B', 'A']
# second iteration
---------------------
stack = ['B', 'A']
character = 'B'

c = stack[-1] = 'A'
stack = ['B']
# third iteration








seq = "BABBA"
print(string_reduction(seq))
"""