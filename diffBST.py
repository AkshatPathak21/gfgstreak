class Solution:
    def absolute_diff(self, root):
        # Your code here
        lst = [float('inf'), 0]
        self.inorder(root, lst)
        return lst[0]
        
    def inorder(self, root, lst):
        if not root:
            return
        
        self.inorder(root.left, lst)
        if lst[1] != 0:
            lst[0] = min(lst[0], abs(root.data - lst[1]))
        lst[1] = root.data
        self.inorder(root.right, lst)