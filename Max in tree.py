# cook your dish here
import sys

class node:
    def __init__(self, data = None):
        self.data = data        #=====>  DATA PART
        self.left = None        #=====>  TO STORE THE LEFT AND RIGHT CHILDREN
        self.right = None

def add(data):
    newnode = node(data)
    return newnode

def maxsize(root):
    if root == None:
        return -(sys.maxsize - 1)
    MAX = root.data
    
    leftMAX = maxsize(root.left)
    rightMAX = maxsize(root.right)
    
    if leftMAX > MAX:
        MAX = leftMAX
    if rightMAX > MAX:
        MAX = rightMAX
    return MAX

root = add(1)
root.left = add(2)
root.right = add(3)
root.left.left = add(4)
root.left.right = add(5)

print(maxsize(root))
