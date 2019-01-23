
class Solution(object):
    def __init__(self):
        self.counter = 0
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return None
        
        l = self.kthSmallest(root.left, k)
        if l is not None: return l
        
        self.counter += 1
        if self.counter == k:
            return root.val
        
        r = self.kthSmallest(root.right, k)
        if r is not None: return r
        
        return None