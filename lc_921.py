
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l, r = 0, 0
        for i in S:
            if i == "(": 
                l += 1
            else: # i == ")": 
                l -= 1
            if l < 0:
                r, l = r + 1, 0
        return l + r


class SolutionA(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
            elif s == "(":
                stack.append("(")
                
        return len(stack)
