class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def begin(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        node.next=self.head
        self.head=node
    def end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        current=self.head
        while(current.next):
            current=current.next
        current.next=node
    def par(self,data,index):
        
        if(index==0):
            self.begin(data)
            return
        pos=0
        current=self.head
        while(current !=None and pos+1!= index):
            current=current.next
            pos+=1
        if current != None:
            node=Node(data)
            node=current.next
            current.next=node
        else:
            print("index not found")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def remove_first_node(self):
        if(self.head == None):
            return
    
        self.head = self.head.next