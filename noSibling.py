class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def noSibling(root):
    # code here
    res=[]
    def util(root):
        if not root:
            return
        util(root.left)
        if not root.left and root.right:
            res.append(root.right.data)
        elif not root.right and root.left:
            res.append(root.left.data)
        util(root.right)
    
    util(root)
    return sorted(res) if len(res) else [-1]