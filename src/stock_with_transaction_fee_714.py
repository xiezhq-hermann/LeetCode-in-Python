class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        wave = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        benefit = [0]
        flag = 0

        for p in wave:
            if p > 0:
                if flag:
                    benefit[-1] += p
                else:
                    benefit.append(p)
                flag = 1
            else:
                if flag:
                    benefit.append(p)
                else:
                    benefit[-1] += p
                flag = 0

        if benefit[-1] < 0:
            benefit.pop()
