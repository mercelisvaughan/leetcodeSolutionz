print("hello world")


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
            

# code out the factorial algorithm
"""
we know we need base cases
we know it is a recursive problem
return the function

factorial is n example of recursion, what is does is multiple the number n by n-1 until it reaches 0
so, 4*3,3*2,2*1 then it stops
"""
def factorial(n):
    if n == 0:
        return 1
        # make a  calculation
    f = n*factorial(n-1)
    print("f = ", f)
    print("n = ", n)
    return f
factorial(4)
"""
f =  1
n =  1
f =  2
n =  2
f =  6
n =  3
f =  24
n =  4
"""

"""
backtracking is a type of recursion that is most useful for traversing tree structures
the following function is a recursive approach to generating all the possible permutations of a given string, s, of a
given length n:
"""
def bitStr(n, s):
    if n == 1: return s
    return [ digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]
print(bitStr(3,'abc'))


