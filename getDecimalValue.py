from typing import Optional
"""

The idea is to loop through the linked list, cast each value as a string, add that casted string value
to an empty string and use the int function to turn it from binary to int
The main operation that we did in this linked list problem
is traversal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        empty_string = ""
        while head:
            num_str = str(head.val)
            empty_string += num_str
            head = head.next
        integer_value = int(empty_string, 2)
        return integer_value