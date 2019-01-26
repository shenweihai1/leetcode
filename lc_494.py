class Solution(object):
    # time limited exceeded
    def basic(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        ans = [0]
        def helper(idx, target):
            if idx == len(nums):
                ans[0] += 1 if target == S else 0
                return
            
            helper(idx + 1, target + nums[idx])
            helper(idx + 1, target - nums[idx])
            
        helper(0, 0)
        return ans[0]
    
    # O(N * M)
    def findTargetSumWays(self, nums, S):
        nums, S = [abs(num) for num in nums], abs(S)
        N = sum(nums)
        if N < S: return 0
        
        dp = [[0] * (N + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(N + 1):
                if i == 0:
                    # +0 = 0 or -0 = 0
                    dp[0][j] = (2 if j == 0 else 1) if abs(nums[0]) == j else 0
                    continue
                    
                dp[i][j] = dp[i - 1][abs(j - nums[i])] + (dp[i - 1][j + nums[i]] if j + nums[i] <= N else 0)
        return dp[len(nums) - 1][S]
