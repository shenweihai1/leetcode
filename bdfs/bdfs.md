### dfs
```
vis = []  # visited nodes
graph = {}

def dfs(u, vis):
    """
    @param: u => initial node
    """
    # if eage cases, continue

    for v in graph[u]:  # neighbours of the node
        if v in vis: continue
        vis.append(v) and dfs(v, vis)
```
Time complexity: O(V + E) + O(graph + retrieval of neighbours)
Space complexity: O(V) + O(graph)

### bfs
```
def bfs():
    q = [u]  # initial node
    vis = []  # visited nodes
    steps = 0  # using for minimum distance
    graph = {}
    while q:
        size = len(q)
        while size > 0:
            u = q.pop(0)
            vis.append(u)  # visited
            for v in graph[u]  # # neighbours of the node
                if v in visited: continue  # or steps <= K
                q.append(v)
            size -= 1
        steps += 1
```
Time complexity: O(V + E) + O(graph + retrieval of neighbours)
Space complexity: O(V) + O(graph)
