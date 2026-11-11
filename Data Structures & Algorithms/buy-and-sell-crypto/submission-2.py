class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_profit = 0, 0, 0 
        for c in range(len(prices)): # O (n) time and O(1) space
            if prices[c] < prices[buy]: 
                buy = c 
                sell = c 
            if prices[c] > prices[sell]:
                sell = c
            if prices[sell] - prices[buy] > max_profit: 
                max_profit = prices[sell] - prices[buy]
        return max_profit