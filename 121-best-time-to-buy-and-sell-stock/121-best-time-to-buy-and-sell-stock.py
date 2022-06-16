class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = max_profit = 0
        for i in range(1, len(prices)):
            current_profit = max(0, current_profit + prices[i] - prices[i - 1])
            max_profit = max(current_profit, max_profit)
        return max_profit
    
            