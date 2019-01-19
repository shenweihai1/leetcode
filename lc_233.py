
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        round = n // 10
        weight = n % 10
        former = 0
        base = 1
        while n // base > 0:
            if weight == 0:
                ans += round * base
            elif weight == 1:
                ans += round * base + former + 1
            else: # weight > 1
                ans += round * base + base
            base = base * 10
            former = n % base
            round = n // (base * 10)
            weight = (n // base) % 10

        return ans


if __name__ == "__main__":
	obj = Solution()
	print(obj.countDigitOne(13))