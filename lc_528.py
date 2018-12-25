
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        cnt = 0
        ans = []
        for i in w:
            ans.append(i + cnt)
            cnt += i
        self.ans = ans
        

    def pickIndex(self):
        """
        :rtype: int
        """
        import random, bisect
        n = random.randint(1,  self.ans[-1])  # a <= N <= b
        return bisect.bisect_left(self.ans, n)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()