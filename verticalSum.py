class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        d = {}
        def traverse(root,key):
            if not root:    return
            if key not in d:
                d[key] = root.data
            else:
                d[key] += root.data
            
            traverse(root.left,key-1)
            traverse(root.right,key+1)
        traverse(root,0)
        li = []
        for k,v in sorted(d.items()):
            li.append(v)
        return li