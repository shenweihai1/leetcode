
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        A, B = A * 'a', B * 'b'
        if len(B) > len(A):  # A is longer
            B, A = A, B
            
        ans = ""
        while A:
            ans += A[:2]
            ans += B[:1]
            A, B = A[2:], B[1:]
        
        # deal with the remaing B
        ans = B[:2] + ans
        B = B[2:]
        n = 4
        while B:
            ans = ans[0:n] + B[0] + ans[n:]
            n += 4
            B = B[1:]
            
        return ans
