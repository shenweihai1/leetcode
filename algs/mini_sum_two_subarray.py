
class Solution:
    # time complexity: O(2 ^ n)
    def find_mini(self, A):
        def helper(idx, target):
            if idx == len(A):
                if abs(2 * target - sum(A)) < ans[0]:
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


if __name__ == "__main__":
    A = [1, 6, 11, 5, 2, 4, 2, 23, 4, 9, 32, 13, 6, 1, 1, 1, 1, 1, 42, 32]
    obj = Solution()
    print(obj.find_mini(A))
    print(obj.find_mini_dp(A))
