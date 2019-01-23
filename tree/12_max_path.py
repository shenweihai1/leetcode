#-*- coding:utf-8
class Solution:
    # 基本思想：对于一个给定节点来说，过该节点的max path为：左max path + 右max path + root.value
    def maxPath(self, root):
        ans = [0]

        def dfs(root):  # 从当前节点出发往下遍历的最大sum
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            ans[0] = max(ans[0], l + r + root.value)
            return max(l, r) + root.value

        dfs(root)
        return ans[0]


if __name__ == "__main__":
    from binarytree import bst
    import random
    root = bst(height=3)
    obj = Solution()
    print(obj.maxPath(root))
    print(root)