# https://leetcode.com/problems/coin-change/submissions/
# Solution => Time Limit exceed
class Solution:
    """
    def coinChange(self, coins, amount):
        import sys
        dp = [[sys.maxsize] * (amount + 1), [sys.maxsize] * (amount + 1)]
        
        # init
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
            
        dp[0][0], dp[1][0] = 0, 0
        
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                left = j 
                while left >= 0:
                    if dp[(i - 1) % 2][left] != sys.maxsize:
                        dp[i % 2][j] = min(dp[i % 2][j], dp[(i - 1) % 2][left] + (j - left) // coins[i])
                    left = left - coins[i]
        return -1 if dp[(len(coins) - 1) % 2][amount] == sys.maxsize else dp[(len(coins) - 1) % 2][amount]
     """

    def coinChange(self, coins, amount):
        dp = [0] + [float("inf")] * amount

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
                    
        return -1 if dp[-1] == float("inf") else dp[-1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.coinChange([346,29,395,188,155,109], 9401))
    print(obj.coinChange([1, 214793434], 2))
