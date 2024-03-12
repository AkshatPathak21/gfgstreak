mat1 = [[1,2,3],[4,5,6],[1,8,9]]

elementMat1 = {}

for i in range(3):
    for j in range(3):
        elementMat1[mat1[i][j]] = True

print(elementMat1)