import collections


class Solution(object):
    def __init__(self):
        self.ans = True

    def dfs(self, p, graph, colors):
        for next in graph[p]:
            if colors[next] == 0:
                colors[next] = -1 * colors[p]
                self.dfs(next, graph, colors)
            else:
                if colors[next] == colors[p]:
                    self.ans = False
                    break

    def possibleBipartition(self, N, dislikes):
        colors = [0] * (N + 1)  # 0 => initial, 1 => read, -1 => blue
        graph = collections.defaultdict(list)
        for pairs in dislikes:
            graph[pairs[0]].append(pairs[1])
            graph[pairs[1]].append(pairs[0])

        for p in range(1, N + 1):
            if colors[p] == 0 and p in graph:
                colors[p] = 1
                self.dfs(p, graph, colors)
                if not self.ans:
                    return False
        return True


if __name__ == "__main__":
	obj = Solution()
	print(obj.possibleBipartition(3, [[1,2],[1,3],[2,3]]))