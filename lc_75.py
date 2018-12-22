
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None
        
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else: # nums[mid] == 2
                self.swap(nums, mid, high)
                high -= 1
            

    def swap(self, nums, s, e):
        nums[s], nums[e] = nums[e], nums[s]