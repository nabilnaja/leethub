class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r, l= len(nums) - 1, 0
        while(l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        