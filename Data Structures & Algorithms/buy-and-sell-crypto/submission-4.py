class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [10,1,5,6,7,1]
        buy = 0
        sell = 1
        max_profit = 0
        while (sell != len(prices)):
            if (sell == buy):
                sell += 1
                continue
            if (prices[buy] > prices[sell]):
                buy = sell
                continue
            
            profit = prices[sell] - prices[buy]
            if (profit >= max_profit):
                max_profit = profit
            sell += 1
            
        return max_profit

            