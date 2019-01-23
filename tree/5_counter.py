#-*- coding:utf-8
class Solution(object):

    def counter(self, root):
        if not root: return 0
        return self.counter(root.left) + self.counter(root.right) + 1

    def counter_leaf(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        return self.counter_leaf(root.left) + self.counter_leaf(root.right)

    def counter_level(self, root, k):  # k: starting from 1
        # using bfs
        steps = 1
        q = [root]
        while q:
            if steps == k:
                return [cur.value for cur in q]

            size = len(q)
            while size > 0:
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                size -= 1
            steps += 1
        return []


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 4)
    root = bst(height=height)
    obj = Solution()
    print(obj.counter(root))
    print(obj.counter_leaf(root))
    print(obj.counter_level(root, 3))
    print(root)
