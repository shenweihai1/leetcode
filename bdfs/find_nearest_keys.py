#-*- coding:utf-8
# Bytedance OA
# 基本思路：将所有的guard做为初始值，使用bfs向外拓展求最小路径，同时不同guard之间不相互影响
# Time complexity: len(guards) * O(m * n)
# Space complexity: O(m * n)
class Solution:
    def findNearestKeys(self, matrix):
        M, N = len(matrix), len(matrix[0])
        dirs = [0, 1, 0, -1, 0]

        q = [(i, j, (i, j)) for i in range(M) for j in range(N) if matrix[i][j] == 2]
        vis = []
        steps = 0
        ans = {uniq: -1 for _, _, uniq in q}
        while q:
            size = len(q)
            while size > 0:
                oi, oj, uniq = q.pop(0)
                vis.append((oi, oj, uniq))
                for d in range(4):
                    i, j = oi + dirs[d], oj + dirs[d + 1]
                    if not (0 <= i <= M - 1) or not (0 <= j <= N - 1): continue
                    u = (i, j, uniq)
                    if u in vis: continue

                    if matrix[i][j] == 3:  # key
                        ans[uniq] = steps + 1
                        continue

                    if matrix[i][j] == 1: continue  # wall
                    matrix[i][j] = 0  # not key or not wall

                    q.append(u)
                size -= 1
            steps += 1
        return ans

if __name__ == "__main__":
    obj = Solution()
    # space: 0, wall: 1, guard: 2, key: 3
    matrix = [
        [0, 1, 1, 0], 
        [2, 2, 1, 2],
        [3, 1, 0, 0],
        [1, 3, 0, 0]
    ]
    print(obj.findNearestKeys(matrix))