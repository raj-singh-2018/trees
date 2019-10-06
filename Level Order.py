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

def levelorder(root):
    Q = queue.Queue()
    Q.put(root)
    while Q.empty() != True:
        temp = Q.get()
        print(temp.data, end = ' ')
        if temp.left != None:
            Q.put(temp.left)
        if temp.right != None:
            Q.put(temp.right)

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.left = add(4)
root.left.right = add(5)

levelorder(root)