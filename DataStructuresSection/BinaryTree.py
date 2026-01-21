class Node:
    def __init__(self, val = None, parent=None, left= None, right = None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        
class BinaryTree():
    def __init__(self):
        self.root = None
    
    def search(self,val):
        curr = self.root
        while(curr and curr.val != val):
            if curr.val < val:
                curr = curr.right
            else: 
                curr = curr.left 
        return curr
    
    def minimun(self):
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def maximum(self):
        curr = self.root 
        while curr and curr.right:
            curr = curr.right
        return curr
    
    def rinsert(self, root, z):
        if not root:
            return z
        if root.left > z.val:
            root.left = self.rinsert(root.left, z )
        else:
            root.right = self.rinsert(root.right, z)
        
        return root
    
    def insert(self, val):
        z = Node(val)
        if self.root is None: # check if there is a tree to traverse
            self.root = z
        curr = self.root
        y = None
        while curr: # find the parent node to which to append z 
            y = curr
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
        if y.val < val: # decide if z is the left or right child 
            y.right = z
        else:
            y.left = z
            
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v  
        if u.parent.left == u:
            u.parent.left = v
        elif u.parent.right == u:
            u.parent.right = v
        if v:
           v.parent = u.parent
            
    def delete(self, u):
        if u.left is None: # if there is only a right subtree subtiture u for u.right
            self.transplant(u, u.right)
        elif u.right is None: # if the is only a left subtree subtiture u for u.left
            self.transplant(u, u.left) 
        else:
            y = self.minimun(u.right) # get the successor 
            if y.parent != u: # if the successor is not the right child of u
                y.right = u.right # replace the succesor with its succesor
                y.right.parent = u.parent
            y = transplant(u,y) # replace the sucessor with u
            y.left = u.left
            y.left.parent = u.parent
            
    def successor(self, z):
        if z and z.right:
            return self.minimun(z)
        y = z.parent
        while y and y.right == z:
            x = y
            y = y.parent
        return y
            
    def predecessor(self,z):
        if z and z.left:
            return self.maximum(z)
        y = z.parent 
        while y and y.left == z:
            x = y
            y = y.parent
        return y    
    
