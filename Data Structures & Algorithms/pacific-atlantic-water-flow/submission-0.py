class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        seen = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        atlantic = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        pacific = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]


        def dfs(r,c):
            if seen[r][c]:
                return atlantic[r][c], pacific[r][c]

            do = [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]
            
            seen[r][c] = 1
            for new_r, new_c in do:
                if new_r < 0 or new_c < 0:
                    pacific[r][c] = 1
                    continue
                if new_r == len(heights) or new_c == len(heights[0]):
                    atlantic[r][c] = 1
                    continue
                if heights[new_r][new_c] <= heights[r][c]:
                    a, p = dfs(new_r,new_c)
                    atlantic[r][c] = max(atlantic[r][c], a)
                    pacific[r][c] = max(pacific[r][c], p)
            
            return atlantic[r][c], pacific[r][c]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                dfs(i,j)

        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i,j])

        return res




                

        