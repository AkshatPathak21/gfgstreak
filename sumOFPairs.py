# My solution 
def countPairs1(mat1, mat2, n, x):
	# code here
	list1 = []
	list2 = []
	count =0
	for i in range(n):
		for j in range(n):
			list1.append(mat1[i][j])
			list2.append(mat2[i][j])
	# print(list1, list2)
	for i in list1:
		for j in list2:
			if i +j ==x:
				count+=1
	return count
				
		        
n = 3
x = 21

mat2 = [[2, 4, 7],
        [9, 10, 12],
        [13, 16, 20]]

mat1 = [[1, 5, 6],
        [8, 10, 11],
        [15, 16, 18]]
 


#Optimized Solution
def countPairs2( mat1, mat2, n, x):
    # Initialize a dictionary to store elements of mat2
    elements_mat2 = {}
    for i in range(n):
        for j in range(n):
            elements_mat2[mat2[i][j]] = True

    # Count pairs
    count = 0
    for i in range(n):
        for j in range(n):
            complement = x - mat1[i][j]
            if complement in elements_mat2:
                count += 1

    return count

print(countPairs1(mat1,mat2,n,x))
print(countPairs2(mat1,mat2,n,x))