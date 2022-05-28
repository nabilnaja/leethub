class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = (nums[0], 0)
        is_larger = True
        for i in range(1, len(nums)):
            if nums[i] > max_num[0]:
                is_larger = nums[i] / 2 >= max_num[0]
                max_num = nums[i], i
                continue
            is_larger = is_larger and  max_num[0] / 2 >= nums[i] 
        return max_num[1] if is_larger else -1
            
            
                
        