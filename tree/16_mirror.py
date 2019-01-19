#-*- coding:utf-8
class Solution(object):

    def mirror(self, root):
        if not root: return None

        root.left, root.right = self.mirror(root.right), self.mirror(root.left)
        return root


if __name__ == "__main__":
    from binarytree import bst
    import random
    root = bst(height=3)
    obj = Solution()
    nodes = root.inorder
    del_nodes = [n.value for n in random.sample(nodes, random.randint(2, 4))]
    print(root)
    print(obj.mirror(root))