class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['-', '+', '*', '/']
        stack = []

        for c in tokens:
            if c in operands:
                val2 = stack.pop()
                val1 = stack.pop()
                if c == '+':
                    stack.append(val1+val2)
                elif c == '-':
                    stack.append(val1-val2)
                elif c == '*':
                    stack.append(val1*val2)
                elif c == '/':
                    stack.append(int(float(val1)/val2))
            else:
                stack.append(int(c))
        return stack[0]
            