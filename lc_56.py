# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        ans = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if not ans or interval.start > ans[-1].end:  # not coverlap
                ans.append(interval)
            else:
                ans[-1].end = max(ans[-1].end, interval.end)
        return ans