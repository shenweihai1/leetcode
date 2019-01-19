#-*- coding:utf-8
# 基本思路：基本和检测同一颗树中是否有subtree
class Solution(object):
    def checkTwoSubtree(self, t1, t2):
        dic = {}
        def dfs(root):
            if not root: return ''
            uniq = '(' + dfs(root.left) + ')' + str(root.value) + '(' + dfs(root.right) + ')'
            dic[uniq] = 1
            return uniq

        uniq = dfs(t2)
        dic = {}
        dfs(t1)
        return uniq in dic
    
    

if __name__ == "__main__":
    from binarytree import bst, tree
    import random
    t1 = bst(height=3, is_perfect=False)
    t2 = bst(height=2, is_perfect=False)
    obj = Solution()
    print(obj.checkTwoSubtree(t1, t1.left))
    print(obj.checkTwoSubtree(t1, t2))
    print(t1)
    print(t2)
