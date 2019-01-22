# Time complexity: O(1)
# Space complexity: O(2 * N)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []
        
    def push(self, num):
        """
        :type x: int
        :rtype: void
        """
        self.A.append(num)
        self.B.append(min(num, self.B[-1]) if self.B else num)

    def pop(self):
        """
        :rtype: void
        """
        if self.A:
            self.A.pop()
            self.B.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.A[-1] if self.A else -1

    def getMin(self):
        """
        :rtype: int
        """
        return self.B[-1] if self.B else -1