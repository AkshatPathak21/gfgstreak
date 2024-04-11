from collections import deque
from functools import reduce

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        q = deque()
        while n > 0:
            q.appendleft(n%2)
            n //= 2
        
        bits = []
        for b in q:
            if not bits:
                bits.append(b)
            else:
                bits.append(bits[-1] ^ b)
        return reduce(lambda v, e: v*2+e, bits, 0)