class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string_integer = ""
        for n in digits:
            string_integer += str(n)
        
        integer = int(string_integer)
        integer += 1

        string_integer = str(integer)
        result = []
        for n in string_integer:
            result.append(int(n))
        return result
