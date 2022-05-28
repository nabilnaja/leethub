class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(1, len(nums) + 1):
            missing = missing ^ i 
        for num in nums:
            missing = missing ^ num
        return missing
            
            
        