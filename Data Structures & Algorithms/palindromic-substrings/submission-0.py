class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s):     
                if s[l] == s[r]:
                    count += 1

                    if r != len(s) - 1:
                        if s[l] == s[r + 1]:
                            count += 1
                else:
                    break
                l -= 1
                r += 1
        
        return count
            