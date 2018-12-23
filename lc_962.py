
import sys
class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        uniq = {}
        for idx, elem in enumerate(A):
            uniq[elem] = [idx, uniq[elem][1] if elem in uniq else idx]

        # (number, right-most index, left-most index)
        uniq = [(k, v[0], v[1]) for k, v in uniq.items()]

        uniq = sorted(uniq, key=lambda x: x[0])

        ans, m = 0, sys.maxsize
        for elem in uniq:
            m = min(m, elem[2])
            ans = max(ans, elem[1] - m)

        return ans
