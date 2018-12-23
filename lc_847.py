
# 
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        q = [(i, 1 << i) for i in range(len(graph))]
        visited = {}
        steps = 0
        while q:
            size = len(q)
            while size > 0:
                p = q.pop(0)
                if p[1] == (1 << len(graph)) - 1:
                    return steps

                for i in graph[p[0]]:
                    next = (i, p[1] | 1 << i)
                    if next not in visited:
                        visited[next] = 1
                        q.append(next)
                size -= 1
            steps += 1
        return steps


obj = Solution()
print(obj.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
print(obj.shortestPathLength([[2,10],[2,7],[0,1,3,4,5,8],[2],[2],[2],[8],[9,11,8,1],[7,6,2],[7],[11,0],[7,10]]))