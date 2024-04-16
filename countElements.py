## Upper bound function to find the index of the element in the sorted array.
def upper_bound(arr, n, target):
    start, end = 0, n # Start and end pointers
    # Binary search
    while start < end:
        mid = start + (end - start) // 2 # Calculate the mid
        if arr[mid] <= target: # If the element is less than or equal to the target
            start = mid + 1 # Move the start pointer to mid + 1
        else: # If the element is greater than the target
            end = mid # Move the end pointer to mid
    if start < n and arr[start] <= target: # If the start is less than n and the element at start is less than or equal to the target
        start += 1 # Increment the start
    return start # Return the start

class Solution:
    def countElements(self, a, b, n, query, q):
        b.sort() # Sort the array
        ans = [] # Initialize the answer
        for i in range(q): # Iterate through the queries
            element = a[query[i]]   # Get the element from the query
            idx = upper_bound(b, n, element)    # Find the index of the element in the sorted array by calling the upperBound function
            ans.append(idx) # Push the index to the answer
        return ans # Return the answer