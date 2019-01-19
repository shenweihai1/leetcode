
# using stack
class Solution:
    def evalRPN(self, A):
        """
        :type tokens: List[str]
        :rtype: int
        """
        div = lambda a, b:  -1 * (abs(a) // abs(b)) if a * b < 0 else abs(a) // abs(b)
        
        def cal(a, b, op):
            a, b = int(a), int(b)
            if op == "+": return b + a
            elif op == "-": return b - a
            elif op == "*": return b * a
            elif op == "/": return div(b, a)
            else:
                raise Exception("err")
            
        sk = []
        for num in A:
            sk.append(cal(sk.pop(), sk.pop(), num) if num in ["+", "-", "*", "/"] else num)
        return int(sk[0])