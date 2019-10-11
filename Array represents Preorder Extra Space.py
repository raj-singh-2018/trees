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
    if data < root.data:
        root.left = addinbst(root.left, data)
    else:
        root.right = addinbst(root.right, data)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

def preorder(b, root):
    if root == None:
        return
    b.append(root.data)
    preorder(b, root.left)
    preorder(b, root.right)
            

root = None
root = addinbst(root, 2)
root = addinbst(root, 4)
root = addinbst(root, 3)

a = [2, 4, 3]
b = []
preorder(b, root)
print('SIZE: ', len(b))
flag = True
if len(a) != len(b):
    flag = False
for _ in range(len(a)):
    if a[_] != b[_]:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')