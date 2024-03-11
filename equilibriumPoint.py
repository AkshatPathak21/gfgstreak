def equilibriumPoint(A, n):
    total_sum = sum(A)
    left_sum = 0
    
    for i in range(n):
        total_sum -= A[i]
        if left_sum == total_sum:
            return i + 1  # 1-based indexing
        left_sum += A[i]
    
    return -1  # No equilibrium point found

# Example usage:
n1 = 5
A1 = [1, 3, 5, 2, 2]
print(equilibriumPoint(A1, n1))  # Output should be 3

n2 = 1
A2 = [1]
print(equilibriumPoint(A2, n2))  # Output should be 1
