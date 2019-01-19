
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        A = sorted(A)
        ans = A[N-1] - A[0];
        for i in range(N - 1):
            a, b = A[i], A[i + 1]
            high = max(A[N-1] - K, a + K)
            low = min(A[0] + K, b - K)
            ans = min(ans, high - low)
        return ans