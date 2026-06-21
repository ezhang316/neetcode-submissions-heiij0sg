class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 1

        seen = [[0 for _ in range(len(matrix[i]))] for i in range(len(matrix))]

        def dfs(i,j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            if prev >= matrix[i][j]:
                return 0
            if seen[i][j] != 0:
                return seen[i][j]

            res1 = dfs(i + 1, j, matrix[i][j])
            res2 = dfs(i - 1, j, matrix[i][j])
            res3 = dfs(i, j + 1, matrix[i][j])
            res4 = dfs(i, j - 1, matrix[i][j])
            seen[i][j] = max(res1, res2, res3, res4) + 1
            nonlocal res
            res = max(res, seen[i][j])
            return seen[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j,-1)
        return res
        