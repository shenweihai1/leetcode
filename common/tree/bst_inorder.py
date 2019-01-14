
# https://github.com/joowani/binarytree
class Solution:
    def __init__(self):
        pass

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        print(root.value),
        self.inorder(root.right)

    def inorder_iterator(self, root):
        pass


if __name__ == "__main__":
    from binarytree import bst
    root = bst(height=3, is_perfect=True)
    obj = Solution()
    obj.inorder(root)
    print(root)
