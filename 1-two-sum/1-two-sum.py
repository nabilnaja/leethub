class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo:
                return [memo[num],i]
            memo[target - num] = i
        
            
            