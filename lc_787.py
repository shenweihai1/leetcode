
import collections

# https://www.youtube.com/watch?v=PLY-lbcxEjg&feature=youtu.be
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, stops):
        import collections
        graph = collections.defaultdict(list)
        for ssrc, ddst, pprice in flights:
            graph[ssrc].append((ddst, pprice))
        # return self.Sol1(n, graph, src, dst, stops)
        # return self.Sol2(n, graph, src, dst, stops)
        return self.Sol3(n, flights, src, dst, stops)

    # DP
    def Sol3(self, n, flights, src, dst, stops):
        # def: dp[k, v] = min cost from src to v with up to k stops
        # equ: dp[k, v] = min(dp[k-1, v], dp[k-1, u] + cost[u, v])
        # init: dp[1, u] = 
        # ans: dp[k, dst]
        pass

    # using DFS
    def Sol2(self, n, graph, src, dst, K):
        def dfs(graph, cur, vis, stops, price):
          if stops == K + 1 or cur == dst:
              ans[0] = min(ans[0], price) if cur == dst else ans[0]
              return 

          for ch, p in graph[cur]:
              if ch not in vis and price + p < ans[0]:  # Add more restrict
                  vis.append(ch)
                  dfs(graph, ch, vis, stops + 1, price + p)
                  vis.pop()

        vis = [src]
        ans = [float("inf")]  # using mutable variables
        dfs(graph, src, vis, 0, 0)
        return -1 if ans[0] == float("inf") else ans[0]

    # using BFS => best way
    # status => (node, price)
    def Sol1(self, n, graph, src, dst, stops):
        q = [(src, 0)]  
        vis = {}
        steps = 0
        ans = float("inf")
        while q:
            size = len(q)
            if steps - 1 > stops:
                break

            while size > 0:
                node, price = q.pop(0)
                if node == dst:
                    ans = min(price, ans)
                
                for next, pprice in graph[node]:
                    if next not in vis or vis[next] > pprice + price:
                        vis[next] = pprice + price
                        q.append((next, pprice + price))
                
                size -= 1
            steps += 1
        return -1 if ans == float("inf") else ans

if __name__ == "__main__":
    obj = Solution()
    # 17
    ba = 10
    bb = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    bc = 6
    bd = 0
    be = 7

    # 200
    a = 3
    b = [[0,1,100],[1,2,100],[0,2,500]]
    c = 0
    d = 2
    e = 1

    print(obj.findCheapestPrice(ba, bb, bc, bd, be))  # 14
    print(obj.findCheapestPrice(a, b, c, d, e))

