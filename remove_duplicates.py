from typing import Optional

"""
Given the head of a sorted linked list, delete all duplicates
such that each element appears only once. 
Return the linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head # our starting node

        while temp: # loop through all the nodes
            while temp.next and temp.next.val == temp.val: # 
                temp.next = temp.next.next
            temp = temp.next
        return head


n1 = ListNode('eggs')
n2 = ListNode('ham')
n3 = ListNode('spam')

n1.next = n2
n2.next = n3

current = n1
while current:
    print(current.val)
    current = current.next