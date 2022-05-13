class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Sub problems : dp(i) number of ways from i, i-1 .. until 0 
        Original problem : dp(n)
        Relate : dp(i) = dp(i-1) + 1 + anther 1 if s[i-1, i] is valid
        Base :  dp(0) = 0 if s[0] == 0 else 1         
        Topological order : 0 , 1, ..., n
        Time : 
        """
        n = len(s)
        @cache
        def dp(i = 0):
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            
            if i == n -1:
                return 1
            
            count_ways = dp(i+1)
            
            if is_valid(s[i:i+2]):
                 count_ways += dp(i+2)
            
            return count_ways
        
        def is_valid(s):
            return True if 0 < int(s) <= 26 else False
        
        return dp()
            
        