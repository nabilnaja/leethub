class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
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
