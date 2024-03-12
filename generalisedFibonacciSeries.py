import numpy as np

class Solution:
    #My Solution using recursion
    def genFibNum(self, a, b, c, n, m):
        # code here 
        ans =  self.gen(n-1, m) * a + self.gen(n-2, m) * b + c
        return ans % m
        
    def gen(self, n, m):
        if n == 1:
            return 1 % m
        elif n == 2:
            return 1 % m
        elif n == 0:
            return 0
        else:
            a = 1
            b = 1
            for _ in range(n - 2):
                a, b = b, (a + b) % m
            return b
    #Solution using Matrices    
    def genFibNum2(self, a, b, c, n, m):
        if n <= 2:
            return 1
        res = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        gen_fib_matrix = np.array([
            [a, b, c],
            [1, 0, 0],
            [0, 0, 1]
        ])
        n -= 2
        while n:
            if n & 1:
                res = np.matmul(res, gen_fib_matrix) % m
            gen_fib_matrix = np.matmul(gen_fib_matrix, gen_fib_matrix) % m
            n >>= 1
        return sum(res[0]) % m

# Example usage:
ob = Solution()
a = 3
b = 3
c = 3
n = 3
m = 5
print(ob.genFibNum(a, b, c, n, m))  # Output: 4
print(ob.genFibNum2(a, b, c, n, m))

a = 2
b = 2
c = 2
n = 4
m = 100
print(ob.genFibNum(a, b, c, n, m))  # Output: 16
print(ob.genFibNum2(a, b, c, n, m))