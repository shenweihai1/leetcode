

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): return False
        
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if s == 'L' or s == 'R']
        if len(A) != len(B): return False
        
        for (s, i), (e, j) in zip(A, B):
            if s != e: return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
            
        return True