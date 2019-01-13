
class MyCalendar:

    def __init__(self):
        self.inters = []
        self.ends = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        idx = bisect.bisect_right(self.ends, start)
        if idx <= len(self.inters) - 1:
            if not (start >= self.inters[idx][1] or self.inters[idx][0] >= end):
                return False
        
        self.inters.insert(idx, (start, end))
        self.ends.insert(idx, end)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)