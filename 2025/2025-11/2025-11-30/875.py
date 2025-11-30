class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2

            time = 0
            for bananas in piles:
                time += math.ceil(float(bananas) / k)
            
            if time <= h:
                result = min(result, k)
                r = k - 1 # now search left portion
            else:
                l = k + 1
        return result

        