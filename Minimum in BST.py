# cook your dish here
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
    
def minval(root):
    curr = root
    while curr.left != None:
        curr = curr.left
    return curr.data

root = None
root = addinbst(root, 50)
root = addinbst(root, 30)
root = addinbst(root, 20)
root = addinbst(root, 40)
root = addinbst(root, 70)
root = addinbst(root, 60)
root = addinbst(root, 10)

inorder(root)
print('MINIMUM VALUE: ', minval(root))