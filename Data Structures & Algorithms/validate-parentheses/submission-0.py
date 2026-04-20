class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for bracket in s:
            if bracket in ['(', '{', '[']:
                seen.append(bracket)
            else:
                top = seen.pop()
                if bracket == ')' and top == '(':
                    continue
                elif bracket == '}' and top == '{':
                    continue
                elif bracket == ']' and top == '[':
                    continue
                else:
                    return False
        
        return True
