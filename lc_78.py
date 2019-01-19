

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res
        