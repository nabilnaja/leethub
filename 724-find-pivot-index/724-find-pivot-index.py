class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0
        prefix_sum = [0] * (n + 1)
        prefix_sum[1] = nums[0]
        for i in range(1, n):
            prefix_sum[i + 1] += prefix_sum[i] + nums[i] 
        print(prefix_sum)
        for i in range(1, n + 1):
            if prefix_sum[i-1] == prefix_sum[n] - prefix_sum[i]:
                return i - 1
        return -1
        