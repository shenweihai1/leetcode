
# class Solution(object):
#     def longestPalindromeSubseq(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) <= 1: return len(s)
#         if s[0] == s[-1]: 
#             return self.longestPalindromeSubseq(s[1:-1]) + 2
#         else:
#             return max(self.longestPalindromeSubseq(s[1:]),
#                        self.longestPalindromeSubseq(s[:-1]),
#                        self.longestPalindromeSubseq(s[1:-1]))

class Solution:
    def longestPalindromeSubseq(self, s):
        N = len(s)
        dp = {}
        for i in range(N)[::-1]:
            for j in range(i, N):
                if i == j: 
                    dp[(i, j)] = 1
                    continue

                if s[i] == s[j]:
                    dp[(i, j)] = 2 + (0 if i + 1 > j - 1 else dp[(i+1, j-1)])
                else:
                    dp[(i, j)] = max(0 if i + 1 > j else dp[(i + 1, j)], 
                                     0 if i + 1 > j - 1 else dp[(i + 1, j - 1)],
                                     0 if i > j - 1 else dp[(i, j -1)])
        
        return dp[(0, N-1)]


if __name__ == "__main__":
    obj = Solution()
    s = "bbbab"
    print(obj.longestPalindromeSubseq(s))
