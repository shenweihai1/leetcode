
class Solution(object):
    # time complexity: O(n * logn)
    def minMeetingRooms(self, intervals):
        import collections
        cd = {}
        for s, e in intervals:
            cd[s], cd[e] = 1, -1

        od = collections.OrderedDict(sorted(cd.items(), key=lambda x:x[0]))
        
        ans = -float("inf")
        print(od)
        rooms = 0
        for _, v in od.items():
            rooms += v
            ans = max(rooms, ans)
        return ans


if __name__ == "__main__":
    intervals = [(0, 4), (1, 2.5), (2, 10), (3, 8), (6, 9), (7, 12), (11, 13)]
    obj = Solution()
    print(obj.minMeetingRooms(intervals))