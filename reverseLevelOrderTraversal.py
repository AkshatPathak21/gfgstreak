from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def reverseLevelOrder(root):
    # code here
    ans = deque()
    q = deque([(root)])
    
    while q:
        qSize = len(q)
        for _ in range(qSize):
            node = q.popleft()
            ans.appendleft(node.data)
            if node.right: q.append(node.right)
            if node.left : q.append(node.left)
        
    return ans