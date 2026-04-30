class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0

        req = {}
        for c in t:
            if c not in req:
                req[c] = 1
            else:
                req[c] += 1
        
        count = 0

        res = ""
        while r < len(s) and l < len(s):

            print("advancing r")

            while count != len(req) and r < len(s):
                if s[r] in req:
                    req[s[r]] -= 1
                    if req[s[r]] == 0:
                        count += 1
                print(s[r])
                print(count, len(req))
                print(req)
                if count != len(req):
                    r += 1
            
            if r >= len(s):
                break
            print("advancing l")
            while s[l] not in req and l < len(s):
                l += 1
            
            if l >= len(s):
                break

            res = res if len(res) < len(s[l:r + 1]) and res else s[l:r + 1]
            print("res = " + res)

            print("moving l until substring not valid")
            while count == len(req):
                if s[l] not in req:
                    l += 1
                    continue
                req[s[l]] += 1
                if req[s[l]] == 1:
                    count -= 1
                l += 1
            r += 1

                
        return res
