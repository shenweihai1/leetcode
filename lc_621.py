class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        nums = [0] * 26
        for l in tasks:
            nums[ord(l) - ord("A")] += 1
        
        mmax_size = 0
        for j in nums:
            mmax_size = mmax_size if mmax_size > j else j
        
        p = 0
        for j in nums:
            p += (1 if j == mmax_size else 0)
            
        return max(len(tasks), (n+1) * (mmax_size-1) + p)