class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
        