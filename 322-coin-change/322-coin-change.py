class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Sub problems : dp(i, r) minimum number of coins from coin i i+1 .. n
        and the r 
        
        Original problem : dp(0,amount) 
        Relate : dp(i) = 
        Base :  r = 0
                i = 
        Topological order : 0 , 1, ..., n ; r, ..., 0
        Time : 
        """
        n = len(coins)
        @cache
        def dp(i = 0, r=amount):
            if r == 0:
                return 0
            if r < 0 or i >=  n:
                return float("inf")
            
            coin_numbers = amount // coins[i]
            
            best = dp(i + 1, r)
            for coin in range(1, coin_numbers + 1):
                current = dp(i + 1, r - (coins[i] * coin)) + coin
                best = min(best, current)
            return best
        #result = dp()
        #return result if result != float("inf") else -1
        """
        Sub problems : dp(i) represent the fewest number of coins needed to make up i money.
        i , i - 1 .. 0
        
        
        Original problem : dp(amount) 
        Relate : dp(i) = 
        Base :  i = 0 return 0
                i <= 0 return inf
        Topological order : i, ..., 0
        Time : 
        """
        @cache
        def dp(i = amount):
            if i < 0: 
                return float("inf")
            if i == 0:
                return 0
            
            best = float("inf") 
            for coin in coins:
                current = dp(i - coin) + 1
                best = min(best, current)
            return best

        result = dp()
        return result if result != float("inf") else -1
                
                
                
                
            
            
        