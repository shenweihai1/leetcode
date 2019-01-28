#-*- coding:utf-8
# basic: 0-1背包, 即物品只能放0 or 1次
# unbounded: 完全背包, 即物品只能放0 - 无穷次

class Solution:
    # time complexity: O(2 ^ N)
    def basic(self, W, V, target):
        def helper(idx, target, val):
            if idx == len(W):
                ans[0] = max(ans[0], val)
                return

            if W[idx] <= target:
                helper(idx + 1, target - W[idx], val + V[idx])

            helper(idx + 1, target, val)
        
        ans = [0]
        helper(0, target, 0)
        return ans[0]

    # time complexity: O(N * M) 
    def basic_dp(self, W, V, target):
        # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i])
        dp = [[0] * (target + 1) for _ in range(len(W))]
        ans = -float("inf")
        for i in range(len(W)):
            for j in range(0, target + 1):
                if i == 0:
                    dp[0][j] = V[0] if j >= W[0] else 0
                    continue
                dp[i][j] = max(dp[i - 1][j - W[i]] + V[i] if j >= W[i] else dp[i - 1][j], dp[i - 1][j])
        return dp[len(W) - 1][target]

    # time complexity: O(2 ^ N)
    def unbounded(self, W, V, target):
        def helper(idx, target, val):
            if idx == len(W):
                ans[0] = max(ans[0], val)
                return

            _ = [helper(idx + 1, target - k * W[idx], val + k * V[idx]) for k in range(target // W[idx] + 1)]

        ans = [0]
        helper(0, target, 0)
        return ans[0]

    # time complexity: O(N * M * avg(j // W[i])) 
    def unbounded_dp(self, W, V, target):
        # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - n * W[i]] + n * V[i])
        dp = [[0] * (target + 1) for _ in range(len(W))]
        ans = -float("inf")
        for i in range(len(W)):
            for j in range(0, target + 1):
                if i == 0:
                    dp[0][j] = max([k * V[0] for k in range(j // W[0] + 1)])
                    continue
                dp[i][j] = max([dp[i - 1][j - k * W[i]] + k * V[i] for k in range(j // W[i] + 1)])
        return dp[len(W) - 1][target]


if __name__ == "__main__":
    obj = Solution()
    W = [1, 1, 2, 2]
    V = [1, 3, 4, 5]
    target = 14
    # V = [1,60,100,120]
    # W = [1,10,20,30]
    # target = 50

    print(obj.basic(W, V, target))
    print(obj.basic_dp(W, V, target))
    print(obj.unbounded(W, V, target))
    print(obj.unbounded_dp(W, V, target))

