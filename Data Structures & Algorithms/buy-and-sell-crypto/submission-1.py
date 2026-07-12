class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =  res = 0
        r = 1
        n = len(prices)
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r+=1
        return res