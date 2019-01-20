
class Solution(object):
    def largestNumber(self, nums):
        nums = ["%s" % i for i in nums]
        for i, m in enumerate(nums):
            for j, n in enumerate(nums[i+1:]):
                j = j + i + 1 # update the index of j
                if "{f}{s}".format(f=m, s=n) < "{f}{s}".format(f=n, s=m):
                    nums[i], nums[j] = n, m
                    m = n
        # special for 0
        is_zero = True
        for i in nums:
            if i != '0':
                is_zero = False
        return "0" if is_zero else "".join(nums)