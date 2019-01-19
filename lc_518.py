

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) == 0:
        	return 1 if amount == 0 else 0

        coins = sorted(coins)
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

        for i in range(1, amount + 1):
        	for j in range(len(coins) - 1)[::-1]:
        		dp[i][j] = dp[i][j + 1] + (dp[i - coins[j]][j] if i - coins[j] >= 0 else 0)

        return dp[amount][0]


if __name__ == "__main__":
	obj = Solution()
	# print(obj.change(25, [1, 2, 5]))
	print(obj.change(10, [5]))
        