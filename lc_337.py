#-*- encoding:utf-8
# 使用两个返回值，而不是两个递归函数的参数，可以避免重复递归

class Solution(object):   
    def rob(self, root):
        if not root:
            return 0    
        return max(self.dfs(root))   

    def dfs(self, root):
        if not root:
            return 0, 0
        ll, lr = self.dfs(root.left)
        rl, rr = self.dfs(root.right)
        return root.val + lr + rr, max(ll + rl, ll + rr, lr + rl, lr + rr)