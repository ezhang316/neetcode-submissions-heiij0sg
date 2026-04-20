class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            palindrome = True

            l, r = i, i

            while l >= 0 and r < len(s):     
                if s[l] == s[r] and palindrome:
                    count += 1

                    if r != len(s) - 1:
                        if s[l] == s[r + 1]:
                            count += 1
                else:
                    palindrome = False
                    if r != len(s) - 1:
                        if s[l] == s[r + 1] and s[l + 1] == s[r]:
                            count += 1
                l -= 1
                r += 1
        
        return count
            