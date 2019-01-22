# Time complexity: O(N*N) N = len(s), Space complexity: O(M) M = len(wordDict)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        h = {w: 1 for w in wordDict}  # optional to use the prefix Tree 
        dp = [False] * (len(s) + 1)
        
        # initialization
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):  # [len(s) - 1, 0]
            for j in range(i, len(s)):
                if s[i:j+1] in h:
                    if dp[j+1]:
                        dp[i] = True
                        break
        return dp[0]