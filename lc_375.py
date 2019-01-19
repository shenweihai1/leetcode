
import sys
class Solution(object):
    def __init__(self):
        self.cache = {}
        
    # minimax
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.recursion(1, n)

    def recursion(self, a, b):
        if a >= b: return 0
        if (a, b) in self.cache: return self.cache[(a, b)]

        mmin = float("inf")
        for i in range(a, b+1):
            res = i + max(self.recursion(a, i-1), self.recursion(i+1, b))
            mmin = min(mmin, res)

        self.cache[(a, b)] = mmin
        return mmin
    # covert the recursion solution into DP