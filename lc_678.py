
# recursive solution
# class Solution:
#     def checkValidString(self, A):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         memo = {}
#         def cur(cnt, s):
#             ccnt, ss = cnt, s
#             if (ccnt, ss) in memo: return memo[(ccnt, ss)]
#             if len(s) == 0: return cnt == 0
            
#             if s[0] == "(":
#                 cnt += 1
#                 ans = cur(cnt, s[1:])
#             elif s[0] == ")":
#                 cnt -= 1
#                 if cnt < 0:
#                     ans = False
#                 else:
#                     ans = cur(cnt, s[1:])
#             else:
#                 ans = cur(cnt, "(" + s[1:]) or cur(cnt, ")" + s[1:]) or cur(cnt, s[1:])

#             memo[(ccnt, ss)] = ans
#             return ans
            
#         return cur(0, A)

class Solution:
    def checkValidString(self, A):
        l, u = 0, 0
        for c in A:
            if c == "(":
                l, u = l + 1, u + 1
            elif c == ")":
                l, u = max(l - 1, 0), u - 1
            else: # "*" introduced
                l, u = max(l - 1, 0), u + 1
            if u < 0:
                return False
        return l == 0
        
        
        