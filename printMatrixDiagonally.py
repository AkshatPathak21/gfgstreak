def matrixDiagonally(mat):
        i,j=0,0
        res=[mat[i][j]]
        r=len(mat)
        c=len(mat[0])
        while i<r-1 or j<c-1:
            if j+1 <c:
                j+=1
                res.append(mat[i][j])
            else:
                i+=1
                res.append(mat[i][j])
            while i+1<r and j-1 >=0:
                i+=1
                j-=1
                res.append(mat[i][j])
            if i+1<r:
                i+=1
                res.append(mat[i][j])
            else:
                j+=1
                res.append(mat[i][j])
            while i-1>=0 and j+1<c:
                i-=1
                j+=1
                res.append(mat[i][j])
        return res

