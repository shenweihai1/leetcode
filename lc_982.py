
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counts = collections.defaultdict(int)
        for i in A:
            for j in A:
                counts[i & j] += 1
        
        ans = 0
        for i in range(65536):
            if counts[i] == 0: continue
            
            for j in A:
                if i & j == 0:
                    ans += counts[i]
        return ans
