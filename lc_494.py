class Solution(object):
    def basic(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        ans = [0]
        def helper(idx, target):
            if idx == len(nums):
                ans[0] += 1 if target == S else 0
                return
            
            helper(idx + 1, target + nums[idx])
            helper(idx + 1, target - nums[idx])
            
        helper(0, 0)
        return ans[0]


if __name__ == "__main__":
    obj = Solution()
    print(obj.basic([40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15], 3))
