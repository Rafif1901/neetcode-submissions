class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_p = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_p:
                max_p = profit
        return max_p