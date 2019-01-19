#-*- coding:utf-8
# https://github.com/joowani/binarytree
# FIXME 缺后序遍历
class Solution:
    def __init__(self):
        pass

    def preorder(self, root):
        if not root: return
        print(root.value),
        self.preorder(root.left)
        self.preorder(root.right)

    def preorder_iterator(self, root):
        if root == None: return
        q, cur = [], root

        while q or cur:
            while cur:
                print(cur.value),
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            cur = cur.right

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        print(root.value),
        self.inorder(root.right)

    def inorder_iterator(self, root):
        if root == None: return
        q, cur = [], root

        while q or cur:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            print(cur.value),
            cur = cur.right


if __name__ == "__main__":
    from binarytree import bst
    root = bst(height=3, is_perfect=True)
    obj = Solution()
    print(root)
    obj.preorder(root)
    print("")
    obj.preorder_iterator(root)
    print("")
    obj.inorder(root)
    print("")
    obj.inorder_iterator(root)

