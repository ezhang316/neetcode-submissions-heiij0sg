class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()
        visited = set()

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    queue.append((m, n))
                    visited.add((m, n))

        step = 0
        while queue:
            for i in range(len(queue)):
                m, n = queue.popleft()

                grid[m][n] = step
                coords = [
                    (m+1,n),
                    (m-1,n),
                    (m,n+1),
                    (m,n-1)
                ]
                for i, j in coords:
                    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                        continue
                    if grid[i][j] == -1:
                        continue
                    if (i,j) in visited:
                        continue
                    queue.append((i,j))
                    visited.add((i,j))
                            
            step += 1