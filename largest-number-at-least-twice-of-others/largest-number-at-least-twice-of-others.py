class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = second_max = max_num_index = -1
        for i in range(0, len(nums)):
            if nums[i] > max_num:
                max_num, second_max = nums[i], max_num
                max_num_index = i
            elif nums[i] > second_max:
                second_max = nums[i]
        return max_num_index if max_num / 2 >= second_max else -1
            
            
                
        