class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for n in tokens:
            if n != '+' and n != '-' and n != '*' and n != '/':
                stack.append(int(n))
            elif n == '+':
                first_val = stack.pop()
                second_val = stack.pop()
                result = int(first_val) + int(second_val)
                stack.append(result)
            elif n == '-':
                first_val = stack.pop()
                second_val = stack.pop()
                result = second_val - first_val
                stack.append(result)
            elif n == '*':
                first_val = stack.pop()
                second_val = stack.pop()
                result = int(first_val) * int(second_val)
                stack.append(result)
            elif n == '/':
                first_val = stack.pop()
                second_val = stack.pop()
                result = abs(second_val) // abs(first_val)
                if first_val <0 and second_val<0:
                    result = result
                elif first_val < 0 or second_val < 0:
                    result = -result
                stack.append(result)
        

     
        return int(stack.pop())