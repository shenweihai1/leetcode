#-*- coding:utf-8
class Solution(object):

    # 一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
    # 基本思想：通过求树高进行计算
    def check_balanced(self, root):
        ans = [True]
        def helper(root):
            if not root: return 0
            l, r = helper(root.left), helper(root.right)
            if abs(l - r) > 1:
                ans[0] = False
            return max(l, r) + 1

        helper(root)
        return ans[0]

    # 基本思路：左边最大的都比根节点小，右边最小的都比跟节点大
    def check_bst(self, root):
        
        ans = [True]
        def helper(root):  # 递归获取二叉树
            if not root: return None, None

            lmax, lmin = helper(root.left)
            rmax, rmin = helper(root.right)
            if lmax and rmin and not (lmax < root.value < rmin):
                ans[0] = False

            return max(lmax or -float("inf"), rmax or -float("inf"), root.value), min(lmin or float("inf"), rmin or float("inf"), root.value)

        helper(root)
        return ans[0]


if __name__ == "__main__":
    from binarytree import bst, tree
    import random
    root = bst(height=3, is_perfect=False) if random.randint(1, 2) % 2 == 1 else tree(height=3, is_perfect=False)
    obj = Solution()
    print(obj.check_balanced(root))
    print(obj.check_bst(root))
    print(root)
    print("expected: is_balanced => %s, is_bst: %s" % (root.is_balanced, root.is_bst))
