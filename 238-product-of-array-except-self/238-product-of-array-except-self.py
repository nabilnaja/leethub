class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time complexity: O(n) 
        Space complexity:  O(n) the size of the result array. 
        """
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            pre = i - 1
            result[i] = nums[pre] * result[pre]
        right = 1
        for i in range(len(nums) - 2, -1, -1):
            next_item = i + 1
            right *= nums[next_item] 
            result[i] = right * result[i]
            
        return result
        