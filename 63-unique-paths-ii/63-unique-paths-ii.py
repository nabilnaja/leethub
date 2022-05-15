class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(i = 0,j = 0):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            
            return dp(i, j+1) + dp(i+1, j)
        return dp()
        