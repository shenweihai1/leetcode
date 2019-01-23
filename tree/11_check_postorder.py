#-*- coding:utf-8
class Solution:
    # 基本思路：将postorder分成左右根三部分
    def checkPostorder(self, postorder):
        if not postorder: return True
        idx = 0
        while idx < len(postorder) - 1:
            if postorder[idx] < postorder[-1]: 
                idx += 1
            else:
                break
        l = idx

        while idx < len(postorder) - 1:
            if postorder[idx] > postorder[-1]: 
                idx += 1
            else:
                break
        r = idx - l

        if l + r + 1 != len(postorder): return False

        return self.checkPostorder(postorder[:l]) and self.checkPostorder(postorder[l:-1])


if __name__ == "__main__":
    from binarytree import bst
    import random
    height = random.randint(3, 5)
    root = bst(height=height)
    obj = Solution()
    print(obj.checkPostorder([i.value for i in root.postorder]))
    print(root)
