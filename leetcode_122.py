# _122. Best Time to Buy and Sell Stock II


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        low = high = None

        for idx in range(1, len(prices)):

            if low == None and prices[idx] > prices[idx-1]:
                low = prices[idx-1]
            elif low is not None and prices[idx] < prices[idx-1]:
                high = prices[idx-1]

            if low is not None and high is not None:
                profit += (high - low)
                low = None
                high = None

        if low is not None and prices[-1] > low:
            profit += (prices[-1] - low)

        return profit
