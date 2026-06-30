class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        
        for c in s1:
            count[c] += 1
        
        l, r, found = 0, 0, 0
        while r < len(s2):
            if s2[r] in count and count[s2[r]] != 0:
                while r < len(s2) and s2[r] in count and count[s2[r]] != 0:
                    count[s2[r]] -= 1
                    found += 1
                    r += 1
                    if found == len(s1):
                        return True
                print("Printing after found")
                print(count)
                print(l, r)
            else:
                r += 1

            while l < r and r < len(s2):
                print("here")
                if s2[l] in count:
                    count[s2[l]] += 1
                    found -= 1
                    print(count)
                    if s2[r] in count and count[s2[r]] != 0:
                        l += 1
                        break
                l += 1

        
        return False

            
