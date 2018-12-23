import heapq
import sys
 
 
# easy implementation of min-heap and max-heap
class Heap(object):
 
    def __init__(self, ttype=1):
        # 0: min-heap, 1: max-heap
        # support the array that contains numeric element
        self.ttype = ttype
        self.vals = []
 
    def push(self, ele):
        ele = sys.maxsize - ele if self.ttype == 1 else ele
        heapq.heappush(self.vals, ele)

    def pop(self):
        smallest = self.first
        heapq.heappop(self.vals)
        return smallest

    @property
    def data(self):
        return [sys.maxsize - i for i in self.vals] if self.ttype == 1 else self.vals
    
    @property
    def first(self):
        # if no first, throw error
        return int(sys.maxsize - self.vals[0]) if self.ttype == 1 else self.vals[0]

    @property
    def size(self):
        return len(self.vals)
 
    @property
    def is_empty(self):
        return len(self.vals) == 0


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = Heap()
        self.min_heap = Heap(0)

    def data(self):
        print(self.max_heap.data)
        print(self.min_heap.data)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.max_heap.is_empty:
            self.max_heap.push(num)
        else:
            if self.min_heap.size == self.max_heap.size:
                if num < self.max_heap.first:
                    self.max_heap.push(num)
                else:
                    self.min_heap.push(num)
            elif self.min_heap.size > self.max_heap.size:
                if num < self.min_heap.first:
                    self.max_heap.push(num)
                else:
                    self.max_heap.push(self.min_heap.pop())  # pop
                    self.min_heap.push(num)
            else:
                if num >= self.max_heap.first:
                    self.min_heap.push(num)
                else:
                    self.min_heap.push(self.max_heap.pop())  # pop
                    self.max_heap.push(num)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.min_heap.size == self.max_heap.size:
            return (self.min_heap.first + self.max_heap.first) / 2.0
        else:
            return self.min_heap.first * 1.0 if self.min_heap.size > self.max_heap.size else self.max_heap.first
 
if __name__ == "__main__":
    arr = [12, 10, 13, 11, 5]
    obj = MedianFinder()
    for i in arr:
        obj.addNum(i)
        print(obj.findMedian())

    # max-heap
    # obj = Heap()
    # arr = [1, 4, 2, 4, 0, -1, -2, -4, 11]
    # for i in arr:
    #     obj.push(i)
    # print(obj.pop())
 
    # print(obj.data)
 
    # # min-heap
    # obj = Heap(0)
    # arr = [1, 4, 2, 4, 0, -1, -2, -4, 11]
    # for i in arr:
    #     obj.push(i)
 
    # print(obj.data)