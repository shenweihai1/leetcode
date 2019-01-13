
class Solution(object):

    def PredictTheWinner(self, nums):
        memo = {}

        def recur(l, r, tag):
            key = (l, r, tag)
            if key in memo: return memo[key]
            if l == r: return nums[l] if tag & 1 else 0
            if tag & 1:
                ans = max(nums[l] + recur(l + 1, r, tag ^ 1), nums[r] + recur(l, r - 1, tag ^ 1))
            else:
                ans = min(recur(l + 1, r, tag ^ 1), recur(l, r - 1, tag ^ 1))
            memo[key] = ans
            return ans

        return 2 * recur(0, len(nums) - 1, 1) >= sum(nums)
    
# tips: using exclusive OR, swap 0, 1