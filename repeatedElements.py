class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        dict1 = {}
        arr1 = []
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                arr1.append(i)
        return arr1