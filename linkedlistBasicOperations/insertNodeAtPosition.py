class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def insertAtPosition(llist, data, position):
        new_node = SinglyLinkedListNode(data)
        dummy = llist

        if llist is None:
            return new_node
        
        count = 0
        
        while dummy.next and count < position - 1:
            count += 1
            dummy = dummy.next

        new_node.next = dummy.next
        dummy.next = new_node

        return llist