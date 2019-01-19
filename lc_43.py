
"""
let's we say we have the string A: 123 and B: 45678

1. reduce the A * B = (B * 3 + 0 * "0") + (B * 2 + 1 * "0") + (B * 1 + 2 * "0")
2. B * 3 = B + B + B = (B + B) + B, B * 2 = B + B, B * 1 = B
3. for now reduce the function multiply to the function plus
"""
class Solution(object):
    def plus(self, A, B):
        A, B = A[::-1], B[::-1]
        car = 0
        ans = ""
        for idx in range(max(len(A), len(B))):
            ac = A[idx] if idx <= len(A) - 1 else 0
            bc = B[idx] if idx <= len(B) - 1 else 0
      
            ans += "%s" % ((int(ac) + int(bc) + car) % 10)
            car = (int(ac) + int(bc) + car) // 10
        ans += "" if car == 0 else "%s" % car
        return ans[::-1]

    def multiply(self, A, B):
        if A == "0" or B == "0": return "0"
        ans = ""
        for idx, ch in enumerate(A[::-1]):
            tmp = ""
            for _ in range(int(ch)):
                tmp = self.plus(tmp, B)
            ans = self.plus(ans, "%s%s" % (tmp, "0" * idx))
        return ans