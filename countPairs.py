class Solution:    
    def countPairs(self,arr, n): 
        from sortedcontainers import SortedList
        A = [ i*v for i, v in enumerate(arr) ]
        S = SortedList()
        ans = 0
        while A:
            v = A.pop()
            ix = S.bisect_left(v)
            ans += ix
            S.add(v)
        return ans