# Time complexity: O(N + QlogN) where N = len(persons), Q = query times
# Space complexity: O(N)
class TopVotedCandidate(object):

    def __init__(self, P, T):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        counter = collections.defaultdict(int)
        leader = []
        
        for po in P:
            counter[po] += 1
            leader.append(po if counter[po] >= (counter[leader[-1]] if leader else -float("inf")) else leader[-1])
        self.leader = leader
        self.times = T

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        r = bisect.bisect_right(self.times, t)
        return self.leader[r - 1]