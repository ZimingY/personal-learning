class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                profit = price - minprice
                maxprofit = max(profit, maxprofit)
        return maxprofit
                
                
                
# float('inf') acts as an unbounded upper value for comparison. This is useful for finding lowest values for something.          
