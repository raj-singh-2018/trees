# cook your dish here
# cook your dish here
# cook your dish here
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def addtobst(root, data):
    if root == None:
        return node(data)
    if data < root.data:
        root.left = addtobst(root.left, data)
    else: 
        root.right = addtobst(root.right, data)
    return root

def check(root, index, a):
    if root == None:
        return
    check(root.left, index, a)
    if root.data == a[index[0]]:
        index[0] += 1
    check(root.right, index, a)
        

root = None
root = addtobst(root, 8)
root = addtobst(root, 3)
root = addtobst(root, 1)
root = addtobst(root, 6)
root = addtobst(root, 4)
root = addtobst(root, 7)
root = addtobst(root, 10)
root = addtobst(root, 14)
root = addtobst(root, 13)

a = [4, 6, 8, 12, 13]
index = [0]

check(root, index, a)
if index[0] == len(a):
    print('YES')
else:
    print('NO')