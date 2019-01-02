class Solution(object):
    def minFlipsMonoIncr(self, A):
        """
        :type S: str
        :rtype: int
        """
        if not A:
            return 0

        left, right, cnt = [], [], 0
        for c in A:
            left.append(cnt)
            if c == '1': cnt += 1

        cnt = 0
        for c in A[::-1]:
            right.append(cnt)
            if c == '0': cnt += 1
        right = right[::-1]

        ans = float("inf")
        for l, r, c in zip(left, right, A):
            mmin = l + r + (1 if c == '0' else 0)
            ans = min(mmin, ans)

        return min(len([c for c in A if c == '1']), ans)