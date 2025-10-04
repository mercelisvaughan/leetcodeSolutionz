class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def insertNodeAtTail(llist, data):
        new_node = SinglyLinkedListNode(data)
        
        if llist is None:  # if list is empty
            return new_node

        current = llist
        while current.next:  # move to the last node
            current = current.next
        current.next = new_node

        return llist  # return the head

