class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
        ]

        res = 0

        for c in characters:
            print("doing: " + c)
            l = r = 0
            misc_count = 0

            while l < len(s) and r < len(s):
                print("start")
                while True:
                    print(s[r])
                    if s[r] != c:
                        misc_count += 1
                    r += 1
                    if r >= len(s) or misc_count > k:
                        if not r >=len(s):
                            if s[r] != c:
                                misc_count -= 1
                            r -= 1
                        break
                
                res = max(res, r - l)

                while True:
                    if s[l] != c:
                        misc_count -= 1
                    l += 1
                    if l >= r or s[l] == c:
                        break

        return res
                


