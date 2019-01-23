#-*- coding:utf-8
class Solution:
    def height(self, root):
        if not root: return 0
        return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 5)
    root = bst(height=height)
    obj = Solution()
    print(obj.height(root))
    print("expected: %s" % (height + 1))
    print(root)