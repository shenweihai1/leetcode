#-*- coding:utf-8
from binarytree import Node

class Solution(object):
    def rebuildTree(self, inorder, preorder):
        if not inorder: return None

        root = inorder.index(preorder[0]) 
        l = self.rebuildTree(inorder[:root], preorder[1:root + 1],)
        r = self.rebuildTree(inorder[root + 1:], preorder[root + 1:],)

        cur = Node(preorder[0])
        cur.left, cur.right = l, r
              
        return cur


if __name__ == "__main__":
    obj = Solution()

    from binarytree import bst
    import random
    height = random.randint(3, 4)
    root = bst(height=height)
    obj = Solution()
    ino, preo, posto = root.inorder, root.preorder, root.postorder
    

    print(obj.rebuildTree([i.value for i in ino], [i.value for i in preo]))
    print("expected: %s" % root)