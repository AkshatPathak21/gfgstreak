def pair_sum(dict, N, arr, sum):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    
    for i in range(N):
        k = sum - arr[i]
        if k in arr and k != arr[i]:
            return True
    
    
    return False