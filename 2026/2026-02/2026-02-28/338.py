class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = bin(i)[2:].count('1')
        return result
        