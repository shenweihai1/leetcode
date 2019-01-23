
# Wish OA
import collections
class Solution:
    # Time complexity: O(m + n)
    def rollTheString(self, A, rolls):
        dnums = collections.defaultdict(int)
        for roll in rolls:
            dnums[roll] += 1

        dsum = [len(rolls)]
        for i in range(1, len(A)):
            dsum.append(dsum[-1] - dnums.get(i, 0))

        rev = lambda ch, num: chr((ord(ch) - ord('a') + num) % 26 + ord('a'))
        return "".join([rev(ch, dsum.pop(0)) for ch in A])


if __name__ == "__main__":
    A = "vwxyz"
    rolls = [1, 3, 3, 5]
    obj = Solution()
    print(obj.rollTheString(A, rolls))


