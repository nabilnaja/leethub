class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity:  O(1)
        """
        fast = nums[0]
        slow = nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
        