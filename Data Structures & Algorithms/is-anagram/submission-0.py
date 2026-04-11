class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        distinct_characters_s = {}

        for c in s:
            distinct_characters_s[c] = distinct_characters_s.get(c, 0) + 1

        distinct_characters_t = {}
        for c in t:
            distinct_characters_t[c] = distinct_characters_t.get(c, 0) + 1
        
        return distinct_characters_t == distinct_characters_s