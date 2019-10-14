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

def secondlargest(root, ans):
    if root == None or ans[1] > 2:
        return
    secondlargest(root.right, ans)
    if ans[1] == 2:
        ans[0] = root.data
    ans[1] += 1
    secondlargest(root.left, ans)

root = None
root = addtobst(root, 10)
root = addtobst(root, 5)
root = addtobst(root, 20)
root = addtobst(root, 30)

ans = [-1, 1]

secondlargest(root, ans)
print(ans[0])