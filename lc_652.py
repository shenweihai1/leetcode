# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        h = {}
        ans = []        
        
        def dfs(root):
            if not root: return ""
            l, r = dfs(root.left), dfs(root.right)
            uniq = "(" + l + ")" + str(root.val) + "(" + r + ")"
            # check duplication
            h[uniq] = h.get(uniq, 0) + 1
            
            if h[uniq] == 2:
                ans.append(root)
            
            return uniq
        
        dfs(root)
        
        return ans
