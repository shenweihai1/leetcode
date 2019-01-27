
class Solution:
    # time complexity: O(2 ^ n)
    # optimize, avoiding overlapping
    def find_mini(self, A):
        def helper(idx, target):
            if idx == len(A):
                if abs(2 * target - S) < ans[0]:
                    ans[0] = abs(2 * target - S)
                return

            path.append(A[idx])
            helper(idx + 1, target + A[idx])
            path.pop()
            helper(idx + 1, target)

        ans, path, S = [float("inf")], [], sum(A)
        helper(0, 0)
        return ans[0]

    # O(m * n) where m = len(A), n = sum(A)
    def find_mini_dp(self, A):
        target = sum(A) // 2 
        dp = [0 if A[0] > ta else A[0] for ta in range(target + 1)] 
        for num in A[1:]:
            for j in range(target, num, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return abs(dp[-1] * 2 - sum(A))

    def another_dp(self, A):
        target = sum(A) // 2
        dp = [0] * (target + 1)  # dp[0] => dp[1] => dp[2] ... dp[len(A) - 1]
        for i in range(len(A)):
            for j in range(target, -1, -1):
                if i == 0:
                    dp[j] = A[i] if j >= A[i] else 0
                    continue

                if j >= A[i]:
                    dp[j] = min(dp[j - A[i]] + A[i], dp[j])
        
        return dp[-1]


if __name__ == "__main__":
    A = [1, 6, 11, 5, 2, 4, 2, 23, 4, 9, 32, 13, 6, 1, 1, 1, 1, 1, 42, 32]
    obj = Solution()
    print(obj.find_mini(A))
    print(obj.find_mini_dp(A))
    print(obj.another_dp(A))
