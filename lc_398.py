
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans, count = -1, 1
        for idx, num in enumerate(self.nums):
            if num == target:
                if ans == -1:
                    ans = idx 
                else:
                    count += 1
                    if random.randint(1, count) == 1:  # inclusive
                        ans = idx
        return ans