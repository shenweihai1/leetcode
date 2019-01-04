

class Solution(object):

    def Soduku(self, matrix):

        options = lambda i, j, matrix: list(set(list(range(1, 10))) - set(matrix[i] + [matrix[k][j] for k in range(9)]))

        def dfs(em_cells, idx, matrix):
            cell = em_cells[idx]
            opts = options(cell[0], cell[1], matrix)

            for o in opts:
                matrix[cell[0]][cell[1]] = o
                if idx == len(em_cells) - 1:
                    return True
                else:
                    if dfs(em_cells, idx + 1, matrix):
                        return True
                    matrix[cell[0]][cell[1]] = 0

            return False

        # using dfs
        em_cells = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]
        return dfs(em_cells=em_cells, idx=0, matrix=matrix)


if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    obj = Solution()
    print(obj.Soduku(grid))
