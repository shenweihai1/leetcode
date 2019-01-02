
def dfs(node, vis):
    for cd in range(cds):  # loop the children of visiting node
        if cd not in vis:
            if cd == enabled:
                vis.append(v)
                dfs(cd, vis)

def bfs(node):
    q = [node]
    vis = []
    steps = 0
    graph = {}
    while q:
        size = len(q)
        while size > 0:
            node = q.pop(0)
            if node == enabled:
                pass

            for next in graph[node]
                if next not in visited:
                    visited.append(next)
                    q.append(next)
            size -= 1
        steps += 1
