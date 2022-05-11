class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        Sub problems : dp(i) represent the number of ways we can paint the fence 0 to i
        Original problem : dp(n) 
        Relate : dp(i) = 
        Base :  i == 1 : k
                i == 2 : k * k
                i == 0 : 0
        Topological order : i, ..., 0
        Time : 
        """
        @cache
        def dp(i = n):
            if i == 1:
                return k
            if i == 2 :
                return k ** 2
            return (k - 1) * (dp(i - 1) + dp(i - 2))
        return dp()
        