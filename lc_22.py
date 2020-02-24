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
        
    
class SolutionA(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dfs(l, r, prefix):
            # always r >= l
            if l > r or l < 0 or r < 0: return
            
            if l == 0 and r == 0:
                ans.append(prefix)
                return
            
            dfs(l, r - 1, prefix + ")")
            dfs(l - 1, r, prefix + "(")
        
        dfs(n, n, "")
        return ans


if __name__ == "__main__":
    obj = SolutionA()
    print(obj.generateParenthesis(4))
