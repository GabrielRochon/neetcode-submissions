class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Single day to buy and single day to sell: we have a window with two pointers (buy and sell)
        # Redefined, the ask is: "Which subarray has the largest difference between its first and last integer"

        # Complexity:
        #   Time: O(n^2), since we evaluate all subarrays (n*(n+1)/2). Not optimal.
        #   Space: O(1), only storing buy, sell and max_profits: all integers

        buy = 0
        sell = 1            # Buying / selling on the same day is pointless, no profit made
        max_profit = 0  

        while sell < len(prices):

            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, (prices[sell] - prices[buy]))
                sell += 1
            else:
                # Window is invalid. Any element in subarray will not yield a valid subarray again
                # Example: [3,5,4,6,1,2]. Buy 3, sell 1: invalid. No need to evaluate 5-1, 4-1, 6-1. Go straight to buy=1 and sell=2
                buy = sell
                sell = buy+1

        return max_profit