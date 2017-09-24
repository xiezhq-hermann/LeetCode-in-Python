class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        take = prices[0]
        profit = 0
        for stock in prices[1:]:
            if stock <= take:
                take = stock
            else:
                profit = max(profit, stock - take)
        return profit
