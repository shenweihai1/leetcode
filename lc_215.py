
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums = nums.sort()
        # return nums[-k]
        
        # using min-heap
        # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/167837/Python-or-tm
        heap = nums[:k]
        heapq.heapify(heap)  # heappush, heappop
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heapreplace(heap, num)
        return heap[0]
        