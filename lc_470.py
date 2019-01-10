
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7() - 1  # [0, 6 + 6 * 7 = 48]
        while num >= 40:
            num = (rand7() - 1) * 7 + rand7() - 1
        
        return num % 10 + 1

# interesting solution: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/210021/Special-and-Amazing-mathematical-solution-1-line
