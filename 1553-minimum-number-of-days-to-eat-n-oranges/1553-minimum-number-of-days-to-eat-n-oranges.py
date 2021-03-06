class Solution:
    def minDays(self, n: int) -> int:
        """
        Sub problems : dp(i) min number of days to eat i orange.
        Original problem : dp(0)
        Relate : dp(i) =  1 + min( (n%2) + dp(n/2), (n%3) + dp(n/3) ) 
        Base :  dp(n) = 0
        Topological order : 0,1,2,..,n
        Time : 
        """
        @cache
        def dp(i = n):
            if i == 1:
                return 1     
            if i <= 0:
                return 0 
            two = (i%2) + dp(i//2)
            three = (i%3) + dp(i//3)
            return 1 + min(two, three) 
        
        return dp()
        