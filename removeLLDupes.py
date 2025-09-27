

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, val):
        current = self.head

        while current:
            if current.data == val:
                return current.data
            current = current.next
        return current
    
    def add(self, val):
        node = Node(val)
        current = self.head
        if current:
            current.next = node
        else:
            current = node
        current

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count