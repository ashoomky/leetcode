class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        result = []

        def backtrack(open_bracket, closed_bracket):
            if open_bracket == closed_bracket == n:
                result.append("".join(stack))
                return
            
            if open_bracket < n:
                stack.append("(")
                backtrack(open_bracket + 1, closed_bracket)
                stack.pop()
            if closed_bracket < open_bracket:
                stack.append(")")
                backtrack(open_bracket, closed_bracket + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result

            
        