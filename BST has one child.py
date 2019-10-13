# cook your dish here
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

def addbst(root, data):
    if root == None:
        return add(data)
    if data < root.data:
        root.left = addbst(root.left, data)
    else:
        root.right = addbst(root.right, data)
    return root

def singlechild(root):
    Q = queue.Queue()
    Q.put(root)
    while Q.empty() != True:
        temp = Q.get()
        if temp.left != None and temp.right != None:
            return False
        if temp.left != None:
            Q.put(temp.left)
        if temp.right != None:
            Q.put(temp.right)
    return True    

root = None
root = addbst(root, 8)
root = addbst(root, 3)
root = addbst(root, 6)
root = addbst(root, 7)
root = addbst(root, 5)

print(singlechild(root))