#-*- coding:utf-8
# 具体题目描述: https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
# 基本思路中序遍历的同时改变指针指向
class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child


class Solution(object):

    def bstToDoublyLinked(self, root):
        def helper(root):
            if not root: return None, None
            lmin, lmax = helper(root.left)
            rmin, rmax = helper(root.right)
            if lmax:
                lmax.right = root
                root.left = lmax

            if rmin:
                root.right = rmin
                rmin.left = root

            return lmin or root, rmax or root

        mmin, _ = helper(root)
        return mmin


if __name__ == "__main__":
    obj = Solution()

    obj = Solution()
    # 自己手动构造一棵树
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(6)
    mmin = obj.bstToDoublyLinked(root)
    while mmin:
        print(mmin.value),
        mmin = mmin.right