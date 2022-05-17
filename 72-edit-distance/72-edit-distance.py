class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        @cache
        def dp(i = 0, j = 0):
            if i == m and j == n:
                return 0
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            down_right = dp(i+1, j+1) if word1[i] == word2[j] else dp(i+1, j+1) + 1
            down = dp(i+1, j) + 1
            right = dp(i, j+1) + 1
            return min(right,down , down_right)
        def dp():
            memo = [[0] * (n+1) for _ in range (m+1)]
            memo_rows = len(memo)
            memo_cols = len(memo[0])
            
            
            
            for i in range(memo_rows):
                memo[i][memo_cols-1] = memo_rows - i - 1
            
            for j in range(memo_cols):
                memo[memo_rows-1][j] = memo_cols - j - 1
                
            for i in range (memo_rows - 2, -1, -1):
                for j in range (memo_cols - 2, -1, -1):
                    right = memo[i][j+1] + 1
                    down = memo[i+1][j] + 1
                    down_right = memo[i+1][j+1] + 1 if word1[i] != word2[j] else memo[i+1][j+1]
                    memo[i][j] = min(right, down, down_right)
                    
            return memo[0][0]
        return dp()
            
            
        