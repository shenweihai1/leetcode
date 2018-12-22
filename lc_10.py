
class Solution(object):
    def isMatch(self, s, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # special case
        if s == "":  # pattern: a*b*.*....
            while len(pattern) >= 2 and pattern[1] == "*":
                pattern = pattern[2:]
            return not pattern

        if len(pattern) <= 1:
            return len(s) == 1 and (pattern == s or pattern == '.')

        # check if next character is star
        if pattern[1] == "*":
            if pattern[0] == '.' or s[0] == pattern[0]:
                if self.isMatch(s[1:], pattern):
                    return True
            if self.isMatch(s, pattern[2:]):
                return True
        else:
            if pattern[0] == '.' or pattern[0] == s[0]:
                if self.isMatch(s[1:], pattern[1:]):
                    return True

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.match("aaab", "a*bb*"))
    print(obj.match("aaab", "a*aaabb*"))
    print(obj.match("aaab", "a*b*"))
    print(obj.match("a.", ""))
    print(obj.match("", ""))
    print(obj.match("a.", "a."))