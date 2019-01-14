
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        dp = [0]
        for c in A: dp.append(dp[-1] + c)
        count = {}
        ans = 0
        for c in dp:
            ans += count.get(c, 0)
            count[c + S] = count.get(c + S, 0) + 1
        return ans