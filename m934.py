def max(A):
    def dfs(i,j,coord):
        if 0<=i<len(A) and 0<=j<len(A[0]) and A[i][j]:
            A[i][j]=0
            coord.append((i,j))
            dire=[0,1,0,-1,0]
            for m in range(len(dire)-1):
                dfs(i+dire[m],j+dire[m+1],coord)


    def bfs(coord):
        dis=0
        while coord:
            i,j=coord.pop()
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if A[x][y]:
                    return dis
                else:
                    A[x][y]=1
                    coord.append((x,y))
            dis+=1

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]:
                coord = []
                dfs(i,j,coord)
                return bfs(coord)


grid=[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(max(grid))


