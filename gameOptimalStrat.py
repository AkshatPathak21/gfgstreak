class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        # we need to try each combination possible
        mem = {}
        def dfs(l,r):
            if (l,r) in mem :
                return mem[(l,r)]
            if l > r :
                return 0 
            poss1 = arr[l] + min(dfs(l+1, r-1), dfs(l+2,r))
            poss2 = arr[r] + min(dfs(l, r-2), dfs(l+1, r-1))
            
            maxi = max(poss1, poss2)
            mem[(l,r)] = maxi
            return mem[(l,r)]
        return dfs(0,n-1)