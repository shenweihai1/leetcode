

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        
        nums = [(num, idx) for idx, num in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])
        
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i][0] + nums[j][0] > target:
                j -= 1
            elif nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                return [nums[i][1], nums[j][1]]
        
        return []