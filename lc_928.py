
# https://buptwc.com/2018/10/21/Leetcode-928-Minimize-Malware-Spread-II/
import collections
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        def dfs(node, vis):
            for n in range(len(graph)):
                if graph[node][n] == 1  and n not in initial and n not in vis:
                    vis.append(n)
                    dfs(n, vis)

        # using bfs instead of dfs
        inf = collections.defaultdict(list)
        del_node = min(initial)
        for node in initial:
            vis = [node]
            dfs(node, vis)
            for n in vis:
                inf[n].append(node)

        max_len = 0
        ans = collections.defaultdict(int)
        for k, v in inf.items():
            if len(v) == 1:
                ans[v[0]] += 1
                if ans[v[0]] > max_len or (ans[v[0]] == max_len and v[0] < del_node):
                    del_node, max_len = v[0], ans[v[0]]
        
        return del_node