class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Sub problems : dp(i) represent the number of palindromic substrings in s[:i].
        Original problem : dp(n) , n = len(s)
        Relate : dp(i) = dp(i-1) + []
        Base : i = 0 return 1, i < 0 =return 0
        Topological order : n , ..., 0
        Time :
        """
        @cache    
        def dp(i,j):
            if i == j: 
                return 1
            if i == j + 1:
                return s[i] == s[j]
            return dp(i+1, j-1) and s[i] == s[j]
        
        
        result = sum([dp(i,j) for i in range(len(s)) for j in range(i,len(s))])
        return result
        