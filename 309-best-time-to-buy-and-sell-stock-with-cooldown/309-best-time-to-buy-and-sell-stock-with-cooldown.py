class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Sub problems : dp(i,cool,hold) max profit from index 0 till i
                        hold mean we are holding stock
                        cool mean we can't sell
        
        Original problem : dp(0,False,False)
        Relate : dp(i,cool,hold) = 
            if cool : do nothing dp(i + 1, False , False)
            if not : 
                if hold -> max(dp(i + 1, True , False) + prices[i], dp(i + 1, False, True) )
                else ->   max(dp(i + 1, False , True) - prices[i], dp(i + 1, False, False) )
        Base :  t = 0 return 0
                i = n return 0
        Topological order : 0 , 1 , n; t , t-1 , 0
        Time : 
        Space : 
        """
        n = len(prices)
        memo = [[0] * 3 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for state in range(3):
                if state == 2:
                    memo[i][state]=memo[i + 1][0]
                    continue
                do_nothing = memo[i + 1][state]
                if state == 1:
                    memo[i][state] = max(memo[i + 1][2] + prices[i], do_nothing)
                elif state == 0:
                    memo[i][state] = max(memo[i + 1][1] - prices[i], do_nothing)
        return memo[0][0]
