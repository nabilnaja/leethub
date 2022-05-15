class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i = 0,j = 0):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            
            return dp(i, j+1) + dp(i+1, j)
        return dp()
        