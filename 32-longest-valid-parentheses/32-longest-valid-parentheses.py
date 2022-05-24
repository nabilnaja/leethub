class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        
        """
        n = len(s)
        memo = [0 for _ in range(n)]
        best = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    memo[i] = memo[i - 2] + 2 if i >= 2 else 2
                elif (i - memo[i - 1]) > 0 and s[i - memo[i - 1] - 1] == '(':
                    memo[i] = memo[i - 1] 
                    memo[i] +=  memo[i - memo[i - 1] - 2] + 2 if (i - memo[i - 1] >= 2) else 2
                best = max(memo[i], best)     
        return best
        