class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
print("After insertions at beginning:")
ll.display() 

ll.insert_at_end(40)
ll.insert_at_end(50)
print("After insertions at end:")
ll.display() 

ll.insert_at_position(25, 2) 
ll.insert_at_position(5, 0)   
ll.insert_at_position(60, 100)  
print("After insertions at specific positions:")
ll.display()
