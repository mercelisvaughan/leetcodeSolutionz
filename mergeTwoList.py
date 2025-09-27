from typing import Optional


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2:
                tail.next = list1.val
                list1 = list1.next
            else:
                tail.next = list2.val
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1.val

        if list2:
            tail.next = list2.val

        return dummy.next