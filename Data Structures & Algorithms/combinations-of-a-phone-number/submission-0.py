class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []
        
        m = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        def rec(i):
            if i == len(digits) - 1:
                print(m)
                return m[digits[i]].copy()
            ret = []
            cur = rec(i + 1)
            for letter in m[digits[i]]:
                for combo in cur:
                    ret.append(letter + combo)
            
            return ret
        
        return rec(0)