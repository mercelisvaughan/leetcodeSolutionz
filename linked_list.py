"""
Linked list is a data structure for storing a sequential collection
You can:
    - Insert at the beginning quickly
The idea is to store the items into individual objects called "nodes"
Each linked list has a head and tail
Each node stores a reference to the next node in the list (a pointer)

"""

class ListNode:
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self._head = None
    def addFirst(self, item):
        self._head = ListNode(item, self._head)
    def removeFirst(self):
        item = self._head.data
        self._head = self._head.pointer
        return item