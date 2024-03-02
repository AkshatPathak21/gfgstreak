def firstElementKTime(a, n, k):
    frequency = {}
    
    for num in a:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] == k:
            return num
    
    return -1

# Example usage:
a1 = [1, 7, 4, 3, 4, 8, 7]
n1 = len(a1)
k1 = 2
print(firstElementKTime(a1, n1, k1))  # Output: 4

a2 = [3, 1, 3, 4, 5, 1, 3, 3, 5, 4]
n2 = len(a2)
k2 = 3
print(firstElementKTime(a2, n2, k2))  # Output: 3
