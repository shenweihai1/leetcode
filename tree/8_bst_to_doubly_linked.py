#-*- coding:utf-8
class Solution(object):

    def bstToDoublyLinked(self, root):
        pass

if __name__ == "__main_":
    obj = Solution()

    from binarytree import bst
    import random
    height = random.randint(3, 4)
    root = bst(height=height)
    obj = Solution()
    

    print(obj.bstToDoublyLinked(root))