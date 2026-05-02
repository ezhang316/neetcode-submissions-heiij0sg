class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = set(s)

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
                        if misc_count > k:
                            r -= 1
                            if s[r] != c:
                                misc_count -= 1
                        break
                print("misc_count = " + str(misc_count))
                print(l, r)
                res = max(res, r - l)

                if s[l] != c:
                    misc_count -= 1
                l += 1

        return res
                


