class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time complexity: O(n)  
        Space complexity:  O(n)        
        """
        max_left = [height[0] for _ in range(len(height))] 
        max_right = [height[len(height) - 1] for _ in range(len(height))]
        
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
        for i in range(len(height) -2 ,-1, -1 ):
            max_right[i] = max(height[i], max_right[i + 1])   
        
        water_volume = 0
        for i in range(1, len(height) - 1):
            current_volume = min(max_left[i], max_right[i]) - height[i]
            if current_volume > 0:
                water_volume += current_volume
        return water_volume
            
        
                    
                
            
            
            
            
        