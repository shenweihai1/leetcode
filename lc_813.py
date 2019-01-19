
class Solution(object):
    def largestSumOfAverages(self, A, K):
        N = len(A)
        if N <= K: return sum(A)
        dp = {}
        for i in range(N): dp[(i, 1)] = sum(A[i:]) / (N - i)
        for j in range(1, K + 1): dp[(N - 1, j)] = A[-1]
        # two loops
        for k in range(2, K + 1):
            for i in range(N - k + 1)[::-1]:
                dp[(i, k)] = max([dp[(j, k - 1)] + sum(A[i:j]) / len(A[i:j]) for j in range(i+1, N - k + 2)])
        return dp[(0, K)]