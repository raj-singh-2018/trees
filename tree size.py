# cook your dish here
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def add(data):
    newnode = node(data)
    return newnode

def treesize(root):
    if root == None:
        return 0
    return 1 + treesize(root.left) + treesize(root.right)

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.left = add(4)
root.left.right = add(5)

print(treesize(root))