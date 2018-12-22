

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        tag2, tag3, tag5 = 0, 0, 0
        ans = []
        ans.append(1)
        for _ in range(n - 1):
        	ans.append(min(2 * ans[tag2], 3 * ans[tag3], 5 * ans[tag5]))

        	while 2 * ans[tag2] <= ans[-1]: tag2 += 1
        	while 3 * ans[tag3] <= ans[-1]: tag3 += 1
        	while 5 * ans[tag5] <= ans[-1]: tag5 += 1
        return ans
