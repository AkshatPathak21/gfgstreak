def maxIndexDiff(self,a, n): 
        ##Your code here
        stack = []
        for i, e in enumerate(a):
            if not stack or e < a[stack[-1]]:
                stack.append(i)
    
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and a[stack[-1]] <= a[i]:
                ans = max(ans, i-stack.pop())
        return ans

n = 9
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]

print(maxIndexDiff(a,n))