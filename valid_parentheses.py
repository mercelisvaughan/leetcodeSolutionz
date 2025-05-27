print("hello world")

# Python program to
# demonstrate stack implementation
# using collections.deque

from collections import deque
parentheses = {'(': ')'}
for key, value in parentheses.items():
    print("this is the dict")
    print(key, value)

stack = deque()

s = "()[]{}"
for letter in s:
    print("letter: " + letter)
    #if letter == parentheses.keys:



# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())



"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

My solution: use a stack, the first in is the first out. We only put something in the stack if it
is a parenthese, and we pop out of the stack if it is a parentheses

so if we have an empty stack that means it is a valid parentheses because we found an even number 
of matches so we were able to stop

if not, we return false bc that means there is a parenthese left in the stack for example

([)]) -> False
because our stack will look like this
s=(
s=(
s=
s=)
we return false bc we found a parenthese and we are at the end of the string
and cannot take anything else out and we have one left

what we're going to do is create a stack, loop through the string
add to the stack if we have a parenthese and pop when we find its match
return true or falso depending on if we have an empty stack or not.
what i want to do is say hey, if this letter in the string is a key in my dict,
add it to the stack
if this letter is the value of my dict, pop whatever is in the stack
((()))
(()))))(())
"""

def valid_parentheses(string) -> bool:
    parentheses = {'(': ')',
                   '{': '}',
                   '[': ']'
                   }
    stack = []
    # ready to loop through string
    for letter in s:
        # if letter is (
        if letter in parentheses.keys():
            stack.append(letter)
        # If it's a closing bracket
        elif letter in parentheses.values():
            # If stack is empty or the top of the stack doesn't match
            # do more logic
            if not stack or parentheses[stack.pop()] != letter:
                return False
    return not stack # check whethere the stack is empty



