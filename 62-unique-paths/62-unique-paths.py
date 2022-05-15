class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i = 0,j = 0):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            
            return dp(i, j+1) + dp(i+1, j)
        
        def dp():
            memo = [[1] * n for _ in range(m)]

            for i in range(m - 2, -1, -1):
                for j in range(n - 2, -1, -1):
                    memo[i][j] = memo[i + 1][j] + memo[i][j + 1]

            return memo[0][0]
                    
                    
        return dp()
        