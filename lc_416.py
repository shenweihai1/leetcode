class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target & 1 == 1: return False
        target = target >> 1
        N = len(nums)
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for i in range(1, N):
            for j in range(target, nums[i] - 1, -1): 
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]
