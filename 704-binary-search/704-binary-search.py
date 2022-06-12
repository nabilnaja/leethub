class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time complexity: O(log n)  
        Space complexity:  O(1)        
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
            
        