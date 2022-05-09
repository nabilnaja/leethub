class Solution:
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
        