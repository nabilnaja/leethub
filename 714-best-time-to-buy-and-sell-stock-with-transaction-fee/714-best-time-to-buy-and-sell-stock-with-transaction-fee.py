class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Sub problems : dp(i,hold) max profit from i to n. hold mean we have an actif transaction 
        Original problem : dp(0, 0)
        Relate : dp(i) =  
        if hold : max(dp(i+1,1), dp(i+1,0) - 2 + prices[i])
        else : max(dp(i+1,1) - prices[i], dp(i+1,0))
        Base :  dp(n, hold) = 0
        Topological order : 0,1,2,..,n
        Time : 
        """
        n = len(prices)
        @cache
        def dp(i = 0, hold = 0):
            if i == n:
                return 0
            return max(dp(i+1,1), dp(i+1,0) - fee + prices[i]) if hold else max(dp(i+1,1) - prices[i], dp(i+1,0))
        return dp()
        