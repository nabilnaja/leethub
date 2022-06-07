class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time complexity: O(n)  
        Space complexity:  O(1)        
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            numbers_sum = numbers[l] + numbers[r]
            if numbers_sum == target:
                return [l + 1, r + 1]
            elif numbers_sum > target:
                r -= 1
            else:
                l += 1
        