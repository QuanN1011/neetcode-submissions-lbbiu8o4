class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            
            elif token in ops:
                num1 = stack.pop()
                num2 = stack.pop()

            if token == '+': stack.append(num2 + num1)
            elif token == '-': stack.append(num2 - num1)
            elif token == '*': stack.append(num2 * num1)
            elif token == '/': stack.append(int(num2 / num1))
        
        return stack.pop()