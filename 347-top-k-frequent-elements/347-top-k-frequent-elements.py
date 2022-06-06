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
        res = []
        for n, c in counter.items():
            bucket[c].append(n)
        for i in range(len(bucket) - 1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
                