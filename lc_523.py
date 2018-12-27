

# https://zxi.mytechroad.com/blog/hashtable/leetcode-523-continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cache = {}
        cache[0] = -1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if k != 0: s = s % k
            if s not in cache.keys():
                cache[s] = i
            else:
                if i - cache[s] > 1:
                    return True
        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.checkSubarraySum([23, 2, 6, 4, 7], 6))
    print(obj.checkSubarraySum([0, 1, 0], 0))
    print(obj.checkSubarraySum([0, 1, 0, 0], 0))
    print(obj.checkSubarraySum([1, 2, 3], 5))
