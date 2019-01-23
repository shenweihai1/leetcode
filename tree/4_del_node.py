#-*- coding:utf-8
# 基本思路：子树根节点肯为某个删除节点的左右子树中的一个(最起始的根节点除外)
class Solution(object):

    def delNodes(self, root, nodes):
        if not root: return []
        ans = [root.value] if root.value not in nodes else []

        def helper(root, nodes):
            if not root: return
            if root.value in nodes:
                if root.left and root.left.value not in nodes:
                    ans.append(root.left.value)

                if root.right and root.right.value not in nodes:
                    ans.append(root.right.value)

            helper(root.left, nodes)
            helper(root.right, nodes)

        helper(root, nodes)
        return ans


if __name__ == "__main__":
    from binarytree import bst
    import random
    root = bst(height=3)
    obj = Solution()
    nodes = root.inorder
    del_nodes = [n.value for n in random.sample(nodes, random.randint(2, 4))]
    print(obj.delNodes(root, del_nodes))
    print(root)
    print("del_nodes: %s" % (del_nodes, ))
