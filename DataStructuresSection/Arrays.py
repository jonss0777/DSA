class Stack:
    def __init__(self, N):
        self.top = -1
        self.arr = [0]*N
        self.size = N
    
    def is_empty(self):
        return self.top == -1  
    
    def push(self,v):
        if self.top+1 < self.size:
            self.arr[self.top+1] = v
            self.top+=1
        else:
            print("Queue is full")
        
    def pop(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            tmp = self.arr[self.top]
            self.top-=1
            return tmp
            
            

class Queue:
    def __init__(self,N):
        self.size = N
        self.arr = [0]*N
        self.l = 0
        self.front = 0
        self.back = 0
    
    def is_empty(self):
        return self.l == 0
            
    def enqueue(self, v):
        if self.l == self.size:
            print("overflow")
        else:
            self.arr[self.back] = v
            self.l = self.l + 1
            self.back = (self.back+1)%self.size
            
        
    def dequeue(self):
        if self.l ==  0:
            print("underflow")
        else:
            x = self.arr[self.front]
            self.l = self.l -1
            self.front = (self.front+1)%self.size
            return x
        
class Deque:
    def __init__(self,N):
        self.arr=[0]*N
        self.size = N
        self.l = 0
        self.front = 0
        self.back = 0
    
    def is_empty(self):
        return self.l == 0
    
    def push_front(self,v):
        if self.l ==  self.size:
            print('overflow')
        else:
            self.front = (self.front-1)%self.size
            self.arr[self.front] = v
            self.l +=1
               
    def push_back(self,v):
        if self.l == self.size:
            print('overflow')
        else:
            self.arr[self.back] = v
            self.back = (self.back+1)%self.size
            self.l +=1
                   
    def pop_front(self):
        if self.is_empty():
            print('underflow')
        else:    
            tmp = self.arr[self.front]
            self.front= (self.front+1)%self.size
            self.l-=1
            return tmp       
    
    def pop_back(self):
        if self.is_empty():
            print('underflow')
        else:
            self.back = (self.back-1)%self.size
            tmp = self.arr[self.back]
            self.l-=1
            return tmp 