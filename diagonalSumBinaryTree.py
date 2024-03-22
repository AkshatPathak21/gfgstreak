class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        #:param root: root of the given tree.
        #no of lefts
        
        ans=[]
        #code here
        def help(root,i):
            if root:
                if len(ans)==i:
                    ans.append(0)
                ans[i]+=root.data
                if root.right:
                    help(root.right,i)
                if root.left:
                    i+=1
                    help(root.left,i)
        help(root,0)
        return ans