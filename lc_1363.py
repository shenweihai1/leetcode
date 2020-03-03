# for the divisor == 3, there should be tricky method
class Solution:
    def largestMultipleOfThree(self, a: List[int]) -> str:
        
        a.sort(reverse=True)
        
        ones = [x for x in a if x % 3 == 1]
        twos = [x for x in a if x % 3 == 2]
        
        tot = sum(a)
        
        if tot % 3 == 1:
            if ones:
                a.remove(ones[-1])
            else:
                a.remove(twos[-1])
                a.remove(twos[-2])  # len(twos) >= 2 because len(ones) == 0
        elif tot % 3 == 2:
            if twos:
                a.remove(twos[-1])
            else:
                a.remove(ones[-1])
                a.remove(ones[-2])
        
        if not a:
            return ""
        # lstrip for the case "000000"
        return "".join(map(str,a)).lstrip("0") or "0"


class Solution2(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        t = 0
        h = {}
        for i, d in enumerate(digits):
            t += d
            h[d] = i
            
        if t == 0: return "0"
        
        if len(digits) == 1:
            return "" if digits[0] % 3 != 0 else str(digits[0])

        if t % 3 == 0:
            return "".join([str(i) for i in sorted(digits, reverse=True)])
        
        # remove one of those digits
        for i in range(1, 10):
            if i in h and i % 3 == t % 3:
                digits = digits[0:h[i]] + digits[h[i] + 1:]
                return "".join([str(i) for i in sorted(digits, reverse=True)])
        
        # if you can not remove any digit
        ans = ""
        for i in range(1, 10):
            if i in h:
                tmp = digits[0:h[i]] + digits[h[i] + 1:]
                v = self.largestMultipleOfThree(tmp)
                if len(v) > len(ans):
                    ans = v
                else:
                    ans = max(ans, v)
                
        return ans
