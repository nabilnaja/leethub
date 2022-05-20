class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Sub problems : dp(i, j) Maximum Length of Repeated Subarray of nums1[i:], nums2[j:].
        Original problem : dp(0, 0)
        Relate : 
        
        Base : i == m or j == n : return 0 
        Topological order : 0 , 1, ..., m ; 1, ..., n
        Time : 
        """
        m, n = len(nums1), len(nums2)
        @cache
        def dp(i, j):
            if i == m or j == n:
                return 0
            return dp(i+1 , j+1) + 1 if nums1[i] == nums2[j] else 0
        #return max([dp(i,j) for i in range(len(nums1)) for j in range(len(nums2))])
        
        def dp():
            memo = [[0] * (n+1) for _ in range (m+1)]
            for i in range (m - 1, -1, -1):
                for j in range (n - 1, -1, -1):
                    if nums1[i] == nums2[j] :
                        memo[i][j] = memo[i+1][j+1] + 1 
            return max(max(row) for row in memo)
        return dp()
        