
# refer to lc_253
class MyCalendarTwo(object):

    def __init__(self):
        self.times = []
        self.counter = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        sidx = bisect.bisect_right(self.times, start)
        eidx = bisect.bisect_left(self.times, end)
        # if having the same time, exit the room at first
        # time: [26, 26, 32, 35] counter: [1, 1, -1, -1]
        # Add (18, 26)
        # time: [18, 26, 26, 26, 32, 35] counter: [1, -1, 1, 1, -1, -1]
        # counter cannot be [1, 1, 1, -1, -1, -1]
        
        self.times.insert(sidx, start)
        self.times.insert(eidx + 1, end)
        
        self.counter.insert(sidx, 1)
        self.counter.insert(eidx + 1, -1)
        
        ans, tmp = -float("inf"), 0
        for c in self.counter:
            tmp += c
            ans = max(tmp, ans)
            if ans == 3:
                self.times.pop(sidx)
                self.times.pop(eidx)
                self.counter.pop(sidx)
                self.counter.pop(eidx)
                return False
            
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)