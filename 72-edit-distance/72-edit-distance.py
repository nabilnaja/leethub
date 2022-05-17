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
            
            result = []
            same = dp(i+1, j+1) if word1[i] == word2[j] else dp(i+1, j+1) + 1
            result.append(same)
            result.append(dp(i+1, j)+ 1)
            result.append(dp(i, j+1)+ 1)
            return min(result)
        
        return dp()
            
            
        