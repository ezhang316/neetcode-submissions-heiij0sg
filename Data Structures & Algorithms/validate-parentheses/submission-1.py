class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for bracket in s:
            if bracket in ['(', '{', '[']:
                seen.append(bracket)
            else:
                if not seen:
                    return False
                top = seen.pop()
                if bracket == ')' and top == '(':
                    continue
                elif bracket == '}' and top == '{':
                    continue
                elif bracket == ']' and top == '[':
                    continue
                else:
                    return False
        
        if seen:
            return False
        return True
