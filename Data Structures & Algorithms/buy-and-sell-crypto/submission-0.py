class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        res = 0

    
        for i in range(1, len(prices)):
        
            # Update the minimum value seen so far  
            minSoFar = min(minSoFar, prices[i])
        
            # Update result if we get more profit                
            res = max(res, prices[i] - minSoFar)
    
        return res
