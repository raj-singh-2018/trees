# cook your dish here
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

def preorder(root):
    if root == None:
        return
    print(root.data, end = ' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = ' ')

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.left = add(4)
root.left.right = add(5)

inorder(root)
print()
preorder(root)
print()
postorder(root)