class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0

        req = defaultdict(int)
        for c in t:
            req[c] += 1
        
        count = 0

        res = ""
        while r < len(s) and l < len(s):

            print(req)
            if s[r] in req:
                req[s[r]] -= 1
                if req[s[r]] == 0:
                    count += 1

            while count != len(req) and r < len(s):
                r += 1
                if s[r] in req:
                    req[s[r]] -= 1
                if req[s[r]] == 0:
                    count += 1
                print(s[r])
                print(count, len(req))
            
            if r >= len(s):
                break
            
            while s[l] not in req and l < len(s):
                l += 1
            
            if l >= len(s):
                break

            res = res if len(res) < len(s[l:r + 1]) else s[l:r + 1]



            req[s[l]] += 1
            if req[s[l]] == 1:
                count -= 1
            l += 1

                
        return res
