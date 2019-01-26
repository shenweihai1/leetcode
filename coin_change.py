class Soltion:
    # get the minimum change of coins
    def basic_dp(self, A, target):
        A = sorted(set(A), reverse=True)
        dp = [float("inf")] * (target + 1)
        for i in range(len(A)):
            for j in range(target, -1, -1):
                if j == 0:
                    dp[j] = float("inf") 
                    continue

                if i == 0:
                    dp[j] = j // A[0] if j % A[0] == 0 else float("inf") 
                    continue
                
                dp[j] = min([dp[j - k * A[i]] + k for k in range(j // A[i] + 1)])

        return dp[-1]


if __name__ == "__main__":
    obj = Solution()
    A = [5, 3, 1]
    target = 14
    print(obj.basic_dp(A, target))
