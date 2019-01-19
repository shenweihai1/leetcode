
# 
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    group = []
                    # using dfs to find the first group and mark as 2
                    self.dfs(i, j, A, group)
                    return self.bfs(group, A)

    def dfs(self, i, j, A, group):
        if i < 0 or i > len(A)-1 or j < 0 or j > len(A) - 1 or A[i][j] != 1:
            return

        A[i][j] = 2
        group.append((i, j))
        dirs = [0, -1, 0, 1, 0]
        for dex in range(4):
            self.dfs(i + dirs[dex], j + dirs[dex + 1], A, group)

    def bfs(self, q, A):
        dirs = [0, 1, 0, -1, 0]
        steps = 0
        while q:
            size = len(q)
            while size > 0:
                p = q.pop(0)
                for dex in range(4):
                    x = p[0] + dirs[dex]
                    y = p[1] + dirs[dex + 1]
                    # not using IN comparision operation
                    if x < 0 or x > len(A) - 1 or y < 0 or y > len(A) - 1 or A[x][y] == 2:
                        continue

                    if A[x][y] == 1:
                        return steps
                    A[x][y] = 2
                    q.append((x, y))

                size -= 1
            steps += 1
        return steps