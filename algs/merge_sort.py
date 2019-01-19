#-*- coding:utf-8
from heapq import merge
import bisect

class Solution:
    def mergeSort(self, nnums):
        N = len(nnums)
        if N <= 1:
            return nnums
        return list(merge(self.mergeSort(nnums[0:N/2]), self.mergeSort(nnums[N/2:])))

    def mergeSortAdv(self, nnums):
        if len(nnums) <= 1:
            return []

        ans, rest = [nnums[0]], nnums[1:]
        while rest:
            u = rest.pop()
            idx = bisect.bisect_right(ans, u)
            ans = ans[0:idx] + [u] + ans[idx:]
        return ans

        
if __name__ == "__main__":
    obj = Solution()
    print(obj.mergeSort([1,2.1,31,4,5,6,7,0]))
    print(obj.mergeSortAdv([1,2.1,31,4,5,6,7,0]))