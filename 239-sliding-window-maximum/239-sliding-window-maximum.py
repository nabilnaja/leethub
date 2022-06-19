class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity:
        Space complexity: 
        """
        if len(nums) * k == 0:
            return []
        
        if k >= len(nums):
            return [max(nums)]
        
        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
        
        deq = deque()
        max_idx = 0
        
        for i in range(k):
            clean_deque(i)
            deq.append(i)
           
            if nums[i] > nums[max_idx]:
                max_idx = i
        res = [nums[max_idx]]
        
        for i in range(k, len(nums)):
            clean_deque(i)
            deq.append(i)
            res.append(nums[deq[0]])
        
        
        return res
            
        
           
        
        
        
        
        