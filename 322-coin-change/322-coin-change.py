class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

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
        amount_size = amount + 1
        memo = [float("inf")] * amount_size
        memo[0] = 0

        for coin in coins:
            for x in range(coin, amount_size):
                memo[x] = min(memo[x], memo[x - coin] + 1)
        return memo[amount] if memo[amount] != float('inf') else -1
                
                
                
                
            
            
        