class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(n log k) 
        Space complexity:  O(k)        
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            heappushpop(heap,nums[i])
        return heap[0]
                
        