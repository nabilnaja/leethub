class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                memo[i][j] = memo[i + 1][j] + memo[i][j + 1]

        return memo[0][0]
        