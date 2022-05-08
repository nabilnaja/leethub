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
        """
        n = len(nums)
        @cache
        def dp(i = n - 1):
            
            if i == 0:
                return 1
            return max([dp(j) for j in range (i) if nums[j] < nums[i]], default=0) + 1
        
        return max(dp(i)  for i in range(len(nums)))
                    
        