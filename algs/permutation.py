# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return [ss] if ss else []
         
        ans = []
        ss = list(ss)
        for idx, num in enumerate(ss):
            ss[idx], ss[0] = ss[0], ss[idx]
            for j in self.Permutation("".join(ss[1:])):
                ans.append(ss[0] + j)
            ss[idx], ss[0] = ss[0], ss[idx]
        return sorted(list(set(ans)))