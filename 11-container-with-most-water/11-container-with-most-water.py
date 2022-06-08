class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best_size = 0
        while l < r:
            current_size = (r - l) * min(height[l], height[r])
            best_size = max(current_size, best_size)
            if height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
        return best_size