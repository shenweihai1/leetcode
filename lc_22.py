"""
intuition:
using context free grammar
rules: S -> (S)|SS|""
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [set([""])]
        for i in range(1, n + 1):
            ans = ["(%s)" % p for p in dp[i-1]]
            for j in range(1, i):
                ans += ["%s%s" % (w, q) for w in dp[j] for q in dp[i-j]]
            dp.append(set(list(ans)))
        return list(dp[n])
        
