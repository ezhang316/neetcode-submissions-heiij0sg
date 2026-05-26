class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = False
        col = False
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    if m != 0:
                        matrix[m][0] = 0
                    else:
                        row = True
                    if n != 0:
                        matrix[0][n] = 0
                    else:
                        col = True
        
        for m in range(1, len(matrix)):
            for n in range(1, len(matrix[0])):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0
        
        if row:
            for m in range(len(matrix)):
                matrix[m][0] = 0
        if col:
            for n in range(len(matrix[0])):
                matrix[0][n] = 0