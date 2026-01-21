from BinaryTree import BinaryTree
from BinaryTree import Node

# Creating a binary tree
#                  7
#                /   \
#              2      9 
#            /  \    /  \ 
#          -3    4  8   100 
#
root = Node(7, None, None, None)
root.left = Node(2, root, None, None)
root.right = Node(9, root, None, None)
root.left.left = Node(-3, root.left, None, None)
root.left.right = Node(4, root.left, None, None)
root.right.left = Node(8, root.right, None,None)
root.right.right = Node(100, root.right, None, None)

# Traverse throught the binary tree

from collections import deque

q = deque([root])
while q:
    x = q.popleft()
    print(x.val)
    if x.left:
        q.append(x.left)
    if x.right:
        q.append(x.right)

t = BinaryTree()
print(t.root)
t.root = root
print(t.root)

print(t.search(7).val)

t.insert(1000)
print(t.maximum().val)
minNode = t.minimun()
print("old min: ", minNode.val)

print(t.delete(minNode))
minNode = t.minimun()
print("new min: ",minNode.val)


