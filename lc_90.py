class Solution:
    # Sol1
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = set()
        for num in nums:
            ans = {(num,)} | {tuple(list(t) + [num]) for t in ans} | ans
        return list(ans) + [[]]

    # Sol2
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = collections.Counter(nums)
        ans = [[]]
        for n, c in count.items():
            tmp = []
            for prev in ans:
                for curr in [[n] * i for i in range(c + 1)]:
                    tmp.append(prev + curr)
            ans = tmp
        return ans