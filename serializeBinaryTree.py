class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution:
    def serialize(self, root):
        arr = []
        def fun(root):
            if root == None:
                return
            fun(root.left)
            arr.append(root.data)
            fun(root.right)
        fun(root)
        return arr
        
    def deSerialize(self, a):
        
        def fun(a, l, r):
            if l > r:
                return
            idx = (l + r) // 2
            root = Node(a[idx])
            root.left = fun(a, l, idx - 1)
            root.right = fun(a, idx + 1, r)
            return root
        return fun(a, 0, len(a) - 1)