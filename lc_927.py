
"""
1. find the # of 1 in A, let N, so, each partition must contain N/3 1s
2. search from the end to the start till the # of 1's == N/3, then we get the only possible seq s, in other words, if the entire seq is valid, the s must be the third partition
3. check if the rest of seq's reqular pattern is 0*s0*s0* or not
"""
class Solution(object):
    
    def threeEqualParts(self, A):
        N, L = sum(A), len(A)
        if N % 3 != 0: return [-1, -1]
        if N == 0: return [0, L - 1]
        
        cnt = 0
        for i in range(L-1, -1, -1):
            if A[i] == 1: cnt += 1
            if cnt == N / 3: break
        # third part => A[i:]

        for j in range(L):
            if A[j] != 0: break
        # first part: A[j:j+len(A[i:])]

        for k in range(j+len(A[i:]), i):
            if A[k] != 0: break
        # second part: A[k:k+len(A[i:])]
        return [j+len(A[i:])-1, k+len(A[i:])] if A[j:j+len(A[i:])] == A[k:k+len(A[i:])] == A[i:] else [-1, -1]