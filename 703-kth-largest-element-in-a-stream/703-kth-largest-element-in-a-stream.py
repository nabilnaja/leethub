class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) <= k:
            self.heap = nums
            heapq.heapify(self.heap)
        else:
            self.heap = nums[:k]
            heapq.heapify(self.heap)
            for i in range(k, len(nums)):
                self.replace(nums[i])
                
            
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            self.replace(val)
        return self.heap[0]
    
    def replace(self, val):
        if val > self.heap[0]:
                    heapq.heapreplace(self.heap, val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)