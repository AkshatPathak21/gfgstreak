class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    def dfs(self, node, curr_path, ans):
        if not node: return
        
        curr_path.append(node.data)
        if not node.left and not node.right:
            ans.append(curr_path[:])
        
        self.dfs(node.left, curr_path, ans)
        self.dfs(node.right, curr_path, ans)
        curr_path.pop()
    
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        if not root: return []
        ans = []
        self.dfs(root, [], ans)
        return ans