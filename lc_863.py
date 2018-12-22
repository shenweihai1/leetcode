# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections 

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # build a undirected graph
        ungraph = collections.defaultdict(set)
        self.get_undirected_graph(ungraph, root)
        # using bfs
        visited = []
        q = [target.val]
        while q and K > 0:
            K -= 1
            p = []
            for c in q:
                visited.append(c)
                for child in ungraph[c]:
                    if child not in visited:
                        p.append(child)
            q = p
        return q

    def get_undirected_graph(self, ungraph, root):
        if root.left:
            ungraph[root.val].add(root.left.val)
            ungraph[root.left.val].add(root.val)
            self.get_undirected_graph(ungraph, root.left)

        if root.right:
            ungraph[root.val].add(root.right.val)
            ungraph[root.right.val].add(root.val)
            self.get_undirected_graph(ungraph, root.right)