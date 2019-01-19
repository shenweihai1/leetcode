
# intuition: try to check if the element - 1 and element + 1 in the array
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        h = {elem: 1 for elem in nums}
        
        vis = {}
        ans = 1
        for num in nums:
            if num in vis:
                continue 
                
            vis[num] = 1
            cur_ans = 1
            
            tmp = num
            while tmp - 1 in h:
                cur_ans += 1
                tmp -= 1
                vis[tmp] = 1
            
            tmp = num
            while tmp + 1 in h:
                cur_ans += 1
                tmp += 1
                vis[tmp] = 1
            
            ans = max(cur_ans, ans)
        
        return ans
                
            