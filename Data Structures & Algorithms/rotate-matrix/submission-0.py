class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        def rotate_ring(n, offset):
            for i in range(n - 1):
                top_left = matrix[0 + offset][i + offset]
                top_right = matrix[i + offset][n - 1 + offset]
                bottom_right = matrix[n - 1 + offset][n - 1 - i + offset]
                bottom_left = matrix[n - 1 - i + offset][0 + offset]

                matrix[i + offset][n - 1 + offset] = top_left
                matrix[n - 1 + offset][n - 1 - i + offset] = top_right
                matrix[n - 1 - i + offset][0 + offset] = bottom_right
                matrix[0 + offset][i + offset] = bottom_left
        
        for i in range(len(matrix)//2):
            rotate_ring(len(matrix) - i*2, i)
            print(matrix)
