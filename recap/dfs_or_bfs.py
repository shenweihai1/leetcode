

def dfs(node, vis):
    for cd in range(cds):  # loop the children of visiting node
        if cd not in vis:
            if cd == enabled:
                vis.append(v)
                dfs(cd, vis)

def bfs(node):
    q = [node]
    steps = 0
    while q:
        size = len(q)
        while size > 0:
            node = q.pop(0)
            if node == enabled:
                q.append(node)
            size -= 1
        steps += 1
