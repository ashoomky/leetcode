class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    
        
        values = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
            }

        result = []

        def backtrack(i, temp):
            if len(temp) == len(digits):
                result.append(temp)
                return
            
            for c in values[digits[i]]:
                backtrack(i + 1, temp + c)

        if digits:
            backtrack(0, "")
        return result

