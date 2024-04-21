class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
            # code here
            l = []
            m = []
            n = []
            for i in array:
                if i<a:
                    l.append(i)
                elif a<=i<=b:
                    m.append(i)
                else:
                    n.append(i)
            if a == b:
                array.sort()
                return array
            
            array[:] = l+m+n