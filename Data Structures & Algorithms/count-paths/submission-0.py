class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        seen = {(m, n) : 1}

        def rec(coords):
            if coords in seen:
                return seen[coords]
            
            x, y = coords
            # print(x,y)
            # print(seen)
            if x + 1 > m:
                seen[(x,y)] = rec((x, y + 1))
            elif y + 1 > n:
                seen[(x,y)] = rec((x + 1, y))
            else:
                seen[(x,y)] = rec((x, y + 1)) + rec((x + 1, y))
            
            return seen[(x,y)]

        return rec((1,1))

