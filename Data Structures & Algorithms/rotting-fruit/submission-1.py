class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def add_to_queue(queue, current, m, n):
            if m + 1 < len(grid) and grid[m + 1][n] == 1 and (m + 1, n) not in current:
                q.append((m + 1, n))
                current.add((m + 1, n))
            
            if m - 1 >= 0 and grid[m - 1][n] == 1 and (m - 1, n) not in current:
                q.append((m - 1, n))
                current.add((m - 1, n))
            
            if n + 1 < len(grid[0]) and grid[m][n + 1] == 1 and (m, n + 1) not in current:
                q.append((m, n + 1))
                current.add((m, n + 1))
            
            if n - 1 >= 0 and grid[m][n - 1] == 1 and (m, n - 1) not in current:
                q.append((m, n - 1))
                current.add((m, n - 1))
        
        q = deque()
        current = set()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 2:
                    add_to_queue(q, current, m, n)
        res = 0
        while q:
            for i in range(len(q)):
                m, n = q.popleft()
                current.remove((m, n))
                grid[m][n] = 2
                add_to_queue(q, current, m, n)
            res += 1

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    return -1
        
        return res



