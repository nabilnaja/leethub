class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time complexity: O(n)  
        Space complexity:  O(1)        
        """
        max_left, max_right= height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1
        water_volume = 0
        while l < r:
            if max_left < max_right:
                l += 1
                current_volume = max_left - height[l]
                max_left = max(max_left, height[l])
            else:
                r -= 1
                current_volume = max_right - height[r]
                max_right = max(max_right, height[r])
            if current_volume > 0:
                water_volume += current_volume
        return water_volume
                
            
            
        