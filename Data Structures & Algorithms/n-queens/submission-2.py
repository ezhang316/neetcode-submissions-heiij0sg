class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        if n < 4:
            return []
        
        res = []

        cols = [0 for _ in range(n)]
        rows = [0 for _ in range(n)]