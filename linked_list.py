"""
Linked list is a data structure for storing a sequential collection
You can:
    - Insert at the beginning quickly
The idea is to store the items into individual objects called "nodes"
Each linked list has a head and tail
Each node stores a reference to the next node in the list (a pointer)

"""

"""
Chapter One:
Linked List - How to create them, 4 basic operations(creating, deleting, inserting, locating), traversal
First Operation is append items to the list (insert)


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Simple class to hold our list, this class holds a reference to the very first node
class SinglyLinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        node = Node(data) # encapsulates 'data' into the node
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node

    def size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count
    
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next