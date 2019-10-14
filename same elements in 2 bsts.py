# cook your dish here
# cook your dish here
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def addinbst(root, data):
    if root == None:
        return node(data)
    if data < root.data:
        root.left = addinbst(root.left, data)
    else:
        root.right = addinbst(root.right, data)
    return root

def inorder1(root, first):
    if root == None:
        return 
    inorder1(root.left, first)
    first.append(root.data)
    inorder1(root.right, first)

def inorder(root, first, index):
    if root == None:
        return 
    inorder(root.left, first, index)
    if root.data != first[index[0]]:
        index[1] = 0
    index[0] += 1
    inorder(root.right, first, index)

root1 = None
root1 = addinbst(root1, 15)
root1 = addinbst(root1, 10)
root1 = addinbst(root1, 20)
root1 = addinbst(root1, 5)
root1 = addinbst(root1, 12)
root1 = addinbst(root1, 25)

root2 = None
root2 = addinbst(root2, 15)
root2 = addinbst(root2, 12)
root2 = addinbst(root2, 20)
root2 = addinbst(root2, 5)
root2 = addinbst(root2, 10)
root2 = addinbst(root2, 25)

first = []
index = [0, 1]
inorder1(root1, first)
inorder(root2, first, index)
print(index[1])