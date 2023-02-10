import heapq

"""
Maintain two heaps, one max and one min, for first and second half of the sorted stream. 
"""
class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
        elif num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2

mf = MedianFinder()
mf.addNum(1);    # arr = [1]
mf.addNum(2);    # arr = [1, 2]
assert mf.findMedian() == 1.5; # return 1.5 (i.e., (1 + 2) / 2)
mf.addNum(3);    # arr[1, 2, 3]
assert mf.findMedian() == 2.0; # return 2.0
