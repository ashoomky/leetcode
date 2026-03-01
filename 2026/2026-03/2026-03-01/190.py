class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_rep = bin(n)[2:]
        string_of_bin = format(n, '032b')
        reversed_string = string_of_bin[::-1]
        
        return int(reversed_string, 2)