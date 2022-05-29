class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n log k) 
        Space complexity:  O(n + k)
        
        Heap solution
        """
        """
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
        
        """
        """
        Time complexity: O(n) 
        Space complexity:  O(n)
        
        Bucket sort solution
        """
        if k == len(nums):
            return nums
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            bucket[c].append(n)
        result = [] 
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        