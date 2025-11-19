class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i, j = 0, 1
    
        while j < len(prices):
            if prices[j] > prices[i]:
                res = prices[j] - prices[i]
                profit = max(profit, res)
            else:
                i = j
            j += 1
        return profit