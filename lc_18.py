
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        A = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                A[nums[i] + nums[j]].append((i, j))  # i < j
                
        for p in range(len(nums)):
            for q in range(p + 1, len(nums)): 
                T = target - nums[p] - nums[q]  # p < q
                if T in A:
                    ans.extend([tuple(sorted([nums[p], nums[q], nums[i], nums[j]])) for i, j in A[T] if i > q])
                            
        return list(set(ans))