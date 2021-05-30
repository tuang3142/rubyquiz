class LinkedList:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

    @classmethod
    def convert_to_linked_list(A):
        head = LinkedList()
        node = head
        for i, v in enumerate(A):
            node.val = v
            if i < len(A) - 1:
                node.next = LinkedList()
            node = node.next
        return head
