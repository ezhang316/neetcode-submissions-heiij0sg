class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        if len(grid) == 1:
            return grid[0][0]
        
        time = grid[0][0]

        mh = [(time,0,0)]

        seen = set()
        seen.add((0,0))

        while True:
            
            _, m, n = heapq.heappop(mh)

            coords = [
                (m - 1, n),
                (m, n - 1),
                (m + 1, n),
                (m, n + 1)
            ]
            smaller_queue = []
            for m, n in coords:
                if m == len(grid) - 1 and n == len(grid[0]) - 1:
                    return max(time, grid[m][n])
                if m >= 0 and n >= 0 and m < len(grid) and n < len(grid[0]) and (m, n) not in seen:
                    if grid[m][n] <= time:
                        seen.add((m, n))
                        smaller_queue.append((m,n))
                    else:
                        seen.add((m, n))
                        heapq.heappush(mh, (grid[m][n], m, n))
            
            while smaller_queue:
                m, n = heapq.heappop(smaller_queue)
                coords = [
                    (m - 1, n),
                    (m, n - 1),
                    (m + 1, n),
                    (m, n + 1)
                ]
                for m, n in coords:
                    if m == len(grid) - 1 and n == len(grid[0]) - 1:
                        return max(time, grid[m][n])
                    if m >= 0 and n >= 0 and m < len(grid) and n < len(grid[0]) and (m, n) not in seen:
                        if grid[m][n] <= time:
                            seen.add((m, n))
                            smaller_queue.append((m,n))
                        else:
                            seen.add((m, n))
                            heapq.heappush(mh, (grid[m][n], m, n))

            
            time = mh[0][0]