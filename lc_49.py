#-*- coding:utf-8
# 基本思路：因为不在乎顺序所以直接用质数乘积表示一个字符串或者其他方式也可以比如: "".join(sorted(s))
# Time complexity: O(sum(len(s))), Space complexity: O(N) N = len(strs)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        groupList = collections.defaultdict(list)
        
        for sstr in strs:
            key = 1
            for c in sstr:
                key *= primes[ord(c) - ord('a')]
            groupList[key].append(sstr)
        return groupList.values()