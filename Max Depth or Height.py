# cook your dish here
# cook your dish here
import queue
class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def dheight(root):
    Q = queue.Queue()
    Q.put(root)
    Q.put(None)
    cnt = 0
    while Q.qsize() > 1:
        temp = Q.get()
        if temp == None:
            cnt += 1
            Q.put(None)
            continue
        if temp.left != None:
            Q.put(temp.left)
        if temp.right != None:
            Q.put(temp.right)
    return cnt

root = None
root = node(1)
root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)
root.left.left.left = node(100)
root.left.left.right = node(200)
root.right = node(3)

print(dheight(root))