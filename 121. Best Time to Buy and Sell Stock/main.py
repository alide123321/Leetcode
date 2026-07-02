class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit, buyPrice = 0, prices[0]

        for i in range(len(prices)):
            if maxProfit < prices[i] - buyPrice:
                maxProfit = prices[i] - buyPrice
            if buyPrice > prices[i]:
                buyPrice = prices[i]
            
        return maxProfit