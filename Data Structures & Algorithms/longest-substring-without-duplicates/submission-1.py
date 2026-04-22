class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0

        if not s:
            return length

        chars = {}

        l, r = 0, 0
        while r < len(s):
            if s[r] in chars.keys():
                chars[s[r]] += 1
            else:
                chars[s[r]] = 1

            if chars[s[r]] > 1:
                while True:
                    chars[s[l]] -= 1
                    if chars[s[l]] < 1:
                        chars.pop(s[l])
                    if s[l] == s[r]:
                        l += 1
                        break
                    l += 1
            length = max(length, len(chars))
            print(length)
            r += 1
        
        return length
            