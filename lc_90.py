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
    # def subsetsWithDup(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     count = collections.Counter(nums)
    #     ans = [[]]
    #     for n, c in count.items():
    #         for i in range(len(ans)):
    #             for curr in [[n] * i for i in range(1, c + 1)]:
    #                 ans.append(ans[i] + curr)
    #     return ans