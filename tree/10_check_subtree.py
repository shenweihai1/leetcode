#-*- coding:utf-8

# 基本思想：用字符串代表一棵树
# Leetcode: https://leetcode.com/problems/find-duplicate-subtrees/
class Solution(object):
    def findDuplicateSubtrees(self, root):
        self.res = []
        self.dic = {}
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return ''

        uniq = '(' + self.dfs(root.left) + ')' + str(root.val) + '(' + self.dfs(root.right) + ')'
        if uniq in self.dic and self.dic[uniq] == 1:
            self.res.append(root)
        self.dic[uniq] = self.dic.get(uniq, 0) + 1
        
        return uniq