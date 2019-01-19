
# https://docs.python.org/2/library/heapq.html
import sys
import heapq
import sys

class TopKHeap(object):
    # implementation the max-heap
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        elem = sys.maxsize - elem
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)  

    def topk(self):
        return [int(sys.maxsize - elem) for elem in self.data]


def main():
    # have to using the max-heap, default using min-heap
    list_num = [1, 2, 10, 4, 5, 6, 7, 8, 9, -1]
    th = TopKHeap(5)

    for i in list_num:
        th.push(i)

    print th.topk()

if __name__ == "__main__":
    main()