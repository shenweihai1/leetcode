
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

    @property
    def data(self):
        return [sys.maxsize - i for i in self.vals] if self.ttype == 1 else self.vals

    @property
    def size(self):
        return len(self.vals)

    @property
    def is_empty(self):
        return len(self.vals) == 0


if __name__ == "__main__":
    # max-heap
    obj = Heap()
    arr = [1, 4, 2, 4, 0, -1, -2, -4, 11]
    for i in arr:
        obj.push(i)

    print(obj.data)

    # min-heap
    obj = Heap(0)
    arr = [1, 4, 2, 4, 0, -1, -2, -4, 11]
    for i in arr:
        obj.push(i)

    print(obj.data)

