class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        res = []
        parts = []

        def is_palindrome(i, j):
            l, r = i, j
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
            
        def rec(i, j):
            if j >= len(s):
                if i == j:
                    res.append(parts.copy())
                return
            
            if is_palindrome(i, j):
                parts.append(s[i : j + 1])
                rec(j + 1, j + 1)
                parts.pop()
            
            rec(i, j + 1)

        rec(0, 0)
        
        return res






        return res