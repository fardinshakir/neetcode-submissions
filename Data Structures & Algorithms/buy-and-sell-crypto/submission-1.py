class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for n in prices:
            lowest_price = min(lowest_price, n); print(lowest_price)
            max_profit = max(max_profit, n - lowest_price)
        return max_profit