class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            check_odd = True

            l, r = i, i

            while l >= 0 and r < len(s):     
                if s[l] == s[r] and check_odd:
                    count += 1
                    if r != len(s) - 1:
                        if s[l] == s[r + 1]:
                            count += 1
                elif not check_odd:
                    if r != len(s) - 1:
                        if s[l] == s[r + 1]:
                            count += 1
                        else:
                            break
                else:
                    if r != len(s) - 1:
                        if s[l] == s[r + 1] and s[l + 1] == s[r]:
                            count += 1
                        else:
                            break
                    check_odd = False
                l -= 1
                r += 1
        
        return count

        # after s[l] != s[r]
        # only the even palindromes will be valid
            