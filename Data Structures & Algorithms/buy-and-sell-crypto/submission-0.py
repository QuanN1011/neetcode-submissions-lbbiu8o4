class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        profit = float('-inf')

        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        
        return profit
