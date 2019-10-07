# cook your dish here
import queue
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def add(data):
    newnode = node(data)
    return newnode

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

def removenode(root, data):
    target = root
    rightmost = root
    prev = root
    cnt = 0
    if root.data == data and root.left == None and root.right == None:
        return None
    Q = queue.Queue()
    Q.put(root)
    
    while Q.empty() != True:
        temp = Q.get()
        if temp.data == data:
            target = temp
        if temp.left != None:
            Q.put(temp.left)
            prev = temp
            rightmost = temp.left
            cnt = 1
        if temp.right != None:
            Q.put(temp.right)
            prev = temp
            rightmost = temp.right
            cnt = 2
            
    if cnt == 1:
        prev.left = None
    else:
        prev.right = None
    
    target.data, rightmost.data = rightmost.data, target.data
    return root

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.left = add(4)
root.left.right = add(5)

inorder(root)
root = removenode(root, 4)
print()
inorder(root)

