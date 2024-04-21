class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        # code here 
        arr =arr1+arr2
        arr = list(set(arr))
        return sorted(arr)