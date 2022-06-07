class MedianFinder:

    def __init__(self):
        self.min_heap, self.max_heap = [], []

    """
    Time complexity: O(log n) 
    Space complexity:  O(n)        
    """
    def addNum(self, num: int) -> None:
        
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        
    """
    Time complexity: O(1)
    Space complexity:  O(n) 
    """
    def findMedian(self) -> float:
        return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()