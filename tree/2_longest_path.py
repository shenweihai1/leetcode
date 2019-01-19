#-*- coding:utf-8
# 基本思想: 对于一个给定节点来说，过该节点的最长路径为：左子树高度 + 右子树高度 + 1
class Solution:

    def longestPath(self, root):
        ans = [0]
        def height(root):
            if not root: return 0
            l, r = height(root.left), height(root.right)
            ans[0] = max(ans[0], l + r + 1)
            return max(l, r) + 1

        height(root)
        return ans[0]


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 5)
    root = bst(height=height)
    obj = Solution()
    print(obj.longestPath(root))
    print(root)