
# Time complexity: O(N), Space complexity: O(N)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for f, t in prerequisites:
            degree[f] += 1
            graph[t].append(f)

        q = [i for i in range(numCourses) if degree[i] == 0]

        ans = 0
        while q:
            e = q.pop(0)
            ans += 1
            for u in graph[e]:
                degree[u] -= 1
                if degree[u] == 0:
                    q.append(u)

        return ans == numCourses