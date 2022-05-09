class Solution:
    """
        Sub problems : dp(i,t,hold) max profit from index 0 till i using t transaction
                        hold mean we are holding stock
        
        Original problem : dp(0,k,0)
        Relate : dp(i,t,hold) = 
            if hold -> max(dp(i + 1, t -1 , 0) + prices[i], dp(i + 1, t, 1) )
            else ->   max(dp(i + 1, t , 1) - prices[i], dp(i + 1, t, 0) )
        Base :  t = 0 return 0
                i = n return 0
        Topological order : 0 , 1 , n; t , t-1 , 0
        Time : O(n*k)
        Spac
    """
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        memo = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for remaining_transaction in range(1, k + 1):
                for holding in range(2):
                    do_nothing = memo[i + 1][remaining_transaction][holding]
                    if holding:
                        memo[i][remaining_transaction][holding] = max(memo[i + 1][ remaining_transaction -1][0] + prices[i], do_nothing)
                    else:
                        memo[i][remaining_transaction][holding] = max(memo[i + 1][ remaining_transaction][1] - prices[i], do_nothing)
        return memo[0][k][0]
        