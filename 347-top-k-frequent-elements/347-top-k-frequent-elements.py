class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        print(counter)
        heap = []
        for char, count in counter.items():   
            heappush(heap,(count,char))
            if len(heap) > k:
                heappop(heap)
            #else: 
        return [x[1] for x in heap]    
        