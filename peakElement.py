  
def peakElement(arr, n):
    # Code here
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
            
        # Check if mid is a peak
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
            
        # If the element to the right of mid is greater, peak must be on the right
        if mid < n - 1 and arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left