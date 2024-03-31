from collections import deque
class Solution:
    def findMaxForN(self, root, n):
        if not root:
            return -1
        lis = []
        q = deque([root])
        while q:
            siz = len(q)
            level = []
            for i in range(siz):
                node = q.popleft()
                level.append(node.key)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lis.extend(level)
        
        ans = 0
        for i in lis:
            if i > ans and i<=n:
                ans = i
        if ans:
            return ans
        return -1