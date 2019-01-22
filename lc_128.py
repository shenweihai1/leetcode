
# intuition: try to check if the element - 1 and element + 1 in the array
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        
        vis = [0] * len(nums)
        h = {num: idx for idx, num in enumerate(nums)}
        ans = 1
        
        for idx, num in enumerate(nums):
            if vis[idx] == 1: continue
            
            tmp, l, r = 1, num - 1, num + 1
            while l in h: vis[h[l]], tmp, l = 1, tmp + 1, l - 1
            while r in h: vis[h[r]], tmp, r = 1, tmp + 1, r + 1
            
            ans = max(tmp, ans)
                
        return ans