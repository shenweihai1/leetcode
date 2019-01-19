#-*- coding:utf-8
class Solution(object):

    def max_width(self, root):
        # using bfs
        steps = 1
        q = [root]
        ans = -float("inf")
        while q:
            size = len(q)
            ans = max(ans, size)
            while size > 0:
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                size -= 1
            steps += 1
        return ans


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 4)
    root = bst(height=height)
    obj = Solution()
    print(obj.max_width(root))
    print(root)
