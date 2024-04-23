class Solution:
    def firstElement (self, n):
        # 1 1
        # 1 0
        a00 = 1
        a01 = 1
        a10 = 1
        a11 = 0
        b00 = 1
        b01 = 1
        b10 = 1
        b11 = 0
        if n == 1:
            return a10
            
        for i in range(1,n):
           l = b10*a00 + b11*a10
           r = b10*a01 + b11*a11
           
           b10 = l % 1000000007
           b11 = r % 1000000007
           
        return b10 % 1000000007