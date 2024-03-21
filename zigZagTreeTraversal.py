from collections import deque
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here
        ans = []
        q = deque()
        q.append([root,0])
        while(q):
            temp = []
            size = len(q)
            while(size):
                node, level = q.popleft()
                temp.append(node.data)
                if node.left:
                    q.append([node.left, level+1])
                if node.right:
                    q.append([node.right, level + 1])
                size-=1
            if level % 2:
                ans+=temp[::-1]
            else:
                ans+=temp
        return ans
    
