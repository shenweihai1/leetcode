# usage of bitwise
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        
        for word in words:
            mask = 0
            for w in word:
                mask |= 1 << (ord(w) - ord('a'))
            d[mask] = max(d.get(mask, 0), len(word))
        
        return max([d[i] * d[j] for i in d for j in d if not(i & j)] or [0])
         