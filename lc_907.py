
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0] * len(A)
        right = [0] * len(A)
        stack = []
        for idx, num in enumerate(A):
            while stack and stack[-1][0] > num:
                stack.pop()
            left[idx] = idx - stack[-1][1] - 1 if stack else idx
            stack.append((A[idx], idx))

        stack = []
        B = A[::-1]
        for idx, num in enumerate(B):
            while stack and stack[-1][0] >= num:
                stack.pop()
            right[idx] = idx - stack[-1][1] - 1 if stack else idx
            stack.append((B[idx], idx))
        right = right[::-1]

        dp = 0
        for l, r, num in zip(left, right, A):
            dp += num * (l * r + l + r + 1)
        return dp % (10 ** 9 + 7)
        
        
        