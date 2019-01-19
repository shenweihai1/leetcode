#-*- coding:utf-8
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None: return None
        
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: return root
        
        return l or (r or None)


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 4)
    root = bst(height=height)
    obj = Solution()
    nodes = root.inorder
    f, s = random.sample(nodes, 2)
    print(obj.lowestCommonAncestor(root, f, s).value)
    print(root)
    print("first: %s, second: %s" % (f.value, s.value))