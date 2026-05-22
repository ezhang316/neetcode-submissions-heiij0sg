class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def get_length(l,r,current):
            if l < 0 or r >= len(s):
                return current

            if s[l] == s[r]:
                return get_length(l - 1, r + 1, s[l] + current + s[r])
            
            return current
        res = ""
        for i in range(len(s)):
            current_odd = get_length(i - 1, i + 1, s[i])
            current_even = ""
            if i < len(s) - 1 and s[i] == s[i + 1]:
                current_even = get_length(i - 1, i + 2, s[i] + s[i + 1])
            current = current_odd if len(current_odd) > len(current_even) else current_even
            if len(res) < len(current):
                res = current
        
        return res