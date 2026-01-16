class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp_prices = prices[:]

            for s, d, p in flights: # source, destination, price
            #if no path, just continue
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p

            prices = temp_prices
        
        return -1 if prices[dst] == float("inf") else prices[dst] 

