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
                    print(stack[-1] / num, int(stack[-1] / num))
                    res = int(stack[-1] / num)
                    stack[-1] = res
            else:
                stack.append(int(token))
        return stack[0]