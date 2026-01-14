class Node:
    def __init__(self, v):
        self.data = v
        self.next = None
        
    
    
class Stack():
    def __init__(self):
        self.head = None
        
    def push(self,v):
        if self.head:
            tmp = Node(v)
            tmp.next = self.head
            self.head = tmp
            
        else:
            self.head = Node(v) 
            
    def pop(self):
        if self.head:
            tmp =self.head.data
            self.head = self.head.next
            return tmp
        else:
            print("Stack is")
            
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, v):
        if self.head:
            self.tail.next = Node(v)
            self.tail = self.tail.next
        else:
            self.head = Node(v)
            self.tail = self.head
    
    def dequeue(self):
        if self.head:
            tmp = self.head.data
            if self.head == self.tail:
                self.head = self.head.next
                self.tail = self.head
            else:
                self.head = self.head.next
            return tmp
        else:
            print("Queue is Empty")
        
 
            
def printL(curr):
    if curr:
        while curr:
            print(curr.data)
            curr = curr.next
    else:
        print("List was empty")
        
        

    