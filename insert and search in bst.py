# cook your dish here
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def add(data):
    newnode = node(data)
    return newnode
    
def addinbst(root, data):
    if root == None:
        return add(data)
    if data > root.data:
        root.right = addinbst(root.right, data)
    elif data < root.data:
        root.left = addinbst(root.left, data)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def findinbst(root, data):
    if root != None:
        if root.data == data:
            return True
        elif data > root.data:
            return findinbst(root.right, data)
        else:
            return findinbst(root.left, data)
    return False

root = None
root = addinbst(root, 5)
root = addinbst(root, 1)
root = addinbst(root, 3)
root = addinbst(root, 4)
root = addinbst(root, 2)
inorder(root)
if findinbst(root, 10):
    print("FOUND")
else:
    print("NOT FOUND")