class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or visited[x][y]:
                return -1
            if grid[x][y] != INF:
                return grid[x][y]
            visited[x][y] = True
            coords = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]
            nearest_chest = INF
            for i, j in coords:
                res = dfs(i, j)
                if res >= 0:
                    nearest_chest = min(nearest_chest, res)
            grid[x][y] = nearest_chest + 1
            if nearest_chest == INF:
                grid[x][y] = INF
            visited[x][y] = False
            return grid[x][y]
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                dfs(m, n)