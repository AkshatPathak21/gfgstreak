class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        
        if n < 3 or m <3:
            return -1
            
        max_sm = 0

        for y in range(1, n-1):
            for x in range(1, m-1):
                temp_sm = 0
                for dy, dx in [(0,0), (-1,0), (-1,-1), (-1, 1), (1,0), (1,-1), (1, 1)]:
                    temp_sm += mat[y+dy][x+dx]
                max_sm = max(max_sm, temp_sm)    
        return max_sm