class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Sub problems : dp(i,j, count) Longest Valid Parentheses for s[i:j] and count is number of unclosed Parentheses.
        i , i - 1 .. 0
        Original problem : dp(n) n is len(s)
        Relate : dp(i, count) =
        s[i] is ')' : 
        s[i] is '('
        
        Base :  i = 0 return 0
                
        Topological order : amount, ..., 0
        Time :
        
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
        