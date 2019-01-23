
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# using DFS
class Solution:
    def __init__(self):
        self.visited = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]

        root = UndirectedGraphNode(node.label)
        self.visited[node] = root  # because for circle
        for elem in node.neighbors:
            root.neighbors.append(self.cloneGraph(elem))
        return root
        