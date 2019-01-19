
class Solution:
    def solveNQueens(self, N):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []

        def full(matrix, i, j, back):
            q, p = i + 1 if back else 0, 0 if back else i + 1
            matrix[i][j] = p
            for m in range(N):
                if matrix[i][m] == q: matrix[i][m] = p
                if matrix[m][j] == q: matrix[m][j] = p
                for x, y in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    if  0 <= x * m + i <= N - 1 and 0 <= y * m + j <= N - 1:
                        if matrix[x * m + i][y * m + j] == q: matrix[x * m + i][y * m + j] = p

        def cur(matrix, i, path):
            if i == N - 1:
                for m in range(N):
                    if matrix[i][m] == 0:
                        path.append(m)
                        tmp = []
                        for x in path:
                            tmp.append("".join(['Q' if x == y else '.' for y in range(N)]))
                        ans.append(tmp)
                        path.pop()
                return 

            for j in range(N):
                if matrix[i][j] == 0:
                    full(matrix, i, j, False)
                    path.append(j)
                    cur(matrix, i + 1, path)
                    path.pop()
                    full(matrix, i, j, True)

        matrix = [[0] * N for _ in range(N)]
        path = []
        cur(matrix, 0, path)
        return ans

