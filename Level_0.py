class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_tail(30)
dll.insert_at_tail(40)

dll.traverse_forward()  # Output: 20 <-> 10 <-> 30 <-> 40 <-> None
dll.traverse_backward() # Output: 40 <-> 30 <-> 10 <-> 20 <-> None
