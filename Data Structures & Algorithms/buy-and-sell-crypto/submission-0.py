class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, n in enumerate(prices):
            for m in prices[i+1:]:
                sum = m - n 
                max_profit = max(sum, max_profit)

        return max_profit