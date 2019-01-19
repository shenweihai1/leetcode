

import collections
import sys
class Solution:

    def minAreaFreeRect(self, A):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def get_len(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) 

        h_vectors = collections.defaultdict(list)
        N = len(A)
        for i in range(N):
            for j in range(i + 1, N):
                vector = (A[j][0] - A[i][0], A[j][1] - A[i][1])
                pos = -1 if vector[1] < 0 or (vector[1] == 0 and vector[0] < 0) else 1
                # the order is important
                h_vectors[(vector[0] * pos, vector[1] * pos)].append((i, j) if pos == 1 else (j, i))

        ans = sys.maxsize
        for vector, lines in h_vectors.items():
            if len(lines) >= 2:
                for i in range(len(lines)):
                    for j in range(i + 1, len(lines)):
                        p1, p2 = A[lines[i][0]], A[lines[i][1]]
                        p3, p4 = A[lines[j][0]], A[lines[j][1]]
                        if (p1[0] - p3[0]) * (p1[0] - p2[0]) + (p1[1] - p3[1]) * (p1[1] - p2[1]) == 0:  # perpendicular 
                            ans = min(get_len(p1, p2) * get_len(p1, p3), ans)

        return 0 if ans == sys.maxsize else ans