class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                num = stack.pop()
                if token == '+':
                    stack[-1] += num
                elif token == '-':
                    stack[-1] -= num
                elif token == '*':
                    stack[-1] *= num
                elif token == '/':
                    stack[-1] //= num
            else:
                stack.append(int(token))
        return int(stack[0])