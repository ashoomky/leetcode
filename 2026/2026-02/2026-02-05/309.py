class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        memo = {} # stores the current max result at the current index
        # own true: we own it
        def dfs(i, own):
            if i >= len(prices):
                return 0
            if (i, own) in memo:
                return memo[(i, own)]
            if own: # sell
                memo[(i, own)] = max(prices[i] + dfs(i+2, False), dfs(i + 1, True))
            else: # buy
                memo[(i, own)] =  max(-prices[i] + dfs(i + 1, True), dfs(i + 1, False))
            return memo[(i, own)]

        return dfs(0, False)
            

            