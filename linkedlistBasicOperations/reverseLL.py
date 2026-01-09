
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def reverseLL(head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next

            curr.next = prev

            prev = curr
            curr = nxt
            
        return prev