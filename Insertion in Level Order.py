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

def addlevel(root, data):
    if root == None:
        root = add(root)
        return root;
    Q = queue.Queue()
    Q.put(root)
    while Q.empty() != True:
        temp = Q.get()
        if temp.left != None:
            Q.put(temp.left)
        else:
            temp.left = add(data)
            break
        if temp.right != None:
            Q.put(temp.right)
        else:
            temp.right = add(data)
            break
    return root
        

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.right = add(4)
root.right.left = add(5)
root.right.right = add(6)

inorder(root)

root = addlevel(root, 100)

print("\nNOW:")
inorder(root)
