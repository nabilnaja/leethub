class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len({x for x in nums}) != len(nums)
        