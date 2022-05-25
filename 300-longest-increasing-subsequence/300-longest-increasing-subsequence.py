class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Sub problems : dp(i) LIS from index i till 0
        
        Original problem : dp(n)
        Relate : dp(i) = max(
                
            )
        Base :  dp(0) = 1
        Topological order : n, n-1, .. , 0
        Time :
        
        n = len(nums)
        memo = [1] * n
        for i in range(1, n):
            memo[i] = max([memo[j] for j in range(i) if nums[j] < nums[i]], default = 0) + 1
                    
        return max(memo) 
        """
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)
            
            else:
                sub[i] = num
        
        return len(sub)
    
                    
        