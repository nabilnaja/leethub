class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n**2)  
        Space complexity:  O(n)        
        """
        nums.sort()
        end = len(nums) - 1
        result = []
        print(nums)
        for current_num_index in range(len(nums)):

            if nums[current_num_index] > 0: 
                break
            
            if current_num_index > 0 and nums[current_num_index - 1] == nums[current_num_index]:
                continue
                
            l, r = current_num_index + 1, end
                
            while l < r: 
                current_sum = nums[current_num_index] + nums[l] + nums[r]
                if current_num_index == 1:
                    print([nums[current_num_index], nums[l], nums[r]])
                if current_sum == 0:
                    result.append([nums[current_num_index], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1   
                elif current_sum > 0:
                    r -= 1    
                else: 
                    l += 1
        
        return(result)
                    
                
                
            
        