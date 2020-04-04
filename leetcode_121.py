# _121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        buy = prices[0]
        sell = buy
        max_profit = sell - buy
        
        for index in range(1, len(prices)):
            if prices[index] < buy:
                buy = prices[index]
                sell = buy
                
            sell = max(sell, prices[index])
            max_profit = max(max_profit, sell - buy)
            
        return max_profit