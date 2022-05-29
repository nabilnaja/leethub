class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n log k) 
        Space complexity:  O(n + k)
        """
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
        