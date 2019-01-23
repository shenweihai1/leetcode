
# based on Longest Increasing Subsequence
class Solution(object):
    def increasingTriplet(self, A):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(A) < 3: return False
        
        min_1, min_2 = float("inf"), float("inf")
        for num in A:
            if num > min_2:
                return True
            elif num > min_1:
                min_2 = num
            else:
                min_1 = num
        
        return False