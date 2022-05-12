class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Sub problems : dp(i, r) represent the number of combinations that make up that amount using the first i coins for cost r 
        Original problem : dp(n) 
        Relate : 
        Base :  i == 1 : k
                i == 2 : k * k
                i == 0 : 0
        Topological order : i, ..., 0
        Time
        """
        n = len(coins)
        @cache
        def dp(i = n - 1, r = amount):
            if r < 0 or i < 0: 
                return 0
            if r == 0:
                return 1
            return dp(i, r - coins[i]) + dp(i - 1, r)
        return dp()