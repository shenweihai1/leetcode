class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) == 0:
        	return 1 if amount == 0 else 0

        dp = []
        # dp[amount][idx]
        # amount starting from 1
        # idx starting from 0
        # initialization
        # idx = len(coins) - 1 or amount = 0
        for j in range(amount + 1):
        	dp.append([1 if j == 0 else 0] * len(coins))  # one possible way when amount = 0
        	if j % coins[-1] == 0:  # integer division
        		dp[j][-1] = 1

        for j in range(1, amount + 1):
        	for i in range(len(coins) - 1)[::-1]:
        		dp[j][i] = dp[j][i + 1] + (dp[j - coins[i]][i] if j - coins[i] >= 0 else 0)

        return dp[amount][0]
