class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                best = max(best, current_streak)

        return best