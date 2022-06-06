class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        counter = Counter(nums)
        heap = []
        
        for num, count in counter.items():
            if len(heap) == k:
                if heap[0][0] < count:
                    heapreplace(heap,(count,num))
                else: 
                    continue
            else:
                heappush(heap,(count,num))
        return [x[1] for x in heap]
            