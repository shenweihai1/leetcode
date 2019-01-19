#-*- coding:utf-8
# 主要思想：遍历到叶子节点并且sum减去每个节点的value等于0即为目标path
# Leetcode: https://leetcode.com/problems/path-sum-ii/
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans, path = [], []
        
        def helper(root, sum, path):
            if not root: return
            if sum == root.val and not root.left and not root.right:
                path.append(root.val)
                ans.append([i for i in path])
                path.pop()
            
            path.append(root.val)
            helper(root.right, sum - root.val, path)
            helper(root.left, sum - root.val, path)
            path.pop()
        
        helper(root, sum, path)
        return ans