
# Time complexity: O(N + N * logN)
class Solution(object):    
    def topKFrequent(self, arr, k):
        count = collections.Counter(arr)
        return sorted(count.keys(), key=count.get, reverse=True)[0:k]
        # return heapq.nlargest(k, count.keys(), key=count.get)