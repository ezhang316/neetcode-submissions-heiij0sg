class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        memo = {}
        
        def rec(i1, i2, i3):

            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]

            if i3 == len(s3) and i1 == len(s1) and i2 == len(s2):
                memo[(i1, i2, i3)] = True
                return True
            
            if i3 == len(s3) or (i1 == len(s1) and i2 == len(s2)):
                memo[(i1, i2, i3)] = False
                return False

            if i1 == len(s1):
                if s2[i2] == s3[i3]:
                    memo[(i1, i2, i3)] = rec(i1, i2 + 1, i3 + 1)
                    return memo[(i1, i2, i3)]
                memo[(i1, i2, i3)] = False
                return False

            if i2 == len(s2):
                if s1[i1] == s3[i3]:
                    memo[(i1, i2, i3)] = rec(i1 + 1, i2, i3 + 1)
                    return memo[(i1, i2, i3)]
                memo[(i1, i2, i3)] = False
                return False

            if s1[i1] != s3[i3] and s2[i2] == s3[i3]:
                memo[(i1, i2, i3)] = rec(i1, i2 + 1, i3 + 1)
                return memo[(i1, i2, i3)]
            if s2[i2] != s3[i3] and s1[i1] == s3[i3]:
                memo[(i1, i2, i3)] = rec(i1 + 1, i2, i3 + 1)
                return memo[(i1, i2, i3)]
            if s2[i2] == s3[i3] and s1[i1] == s3[i3]:
                memo[(i1, i2, i3)] = rec(i1 + 1, i2, i3 + 1) or rec(i1, i2 + 1, i3 + 1)
                return memo[(i1, i2, i3)]

            memo[(i1, i2, i3)] = False
            return False

        return rec(0,0,0)
