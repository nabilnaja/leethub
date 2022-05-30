class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                current_num = num

                while current_num + 1 in nums_set:
                    count += 1
                    current_num += 1
                best = max(best, count)
            
        return best
            
            
                
                
        