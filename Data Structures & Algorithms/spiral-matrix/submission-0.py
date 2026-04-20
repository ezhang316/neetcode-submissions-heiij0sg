class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        right, bottom, left, top = len(matrix[0]) - 1, len(matrix) - 1, 0, 0
        x, y = 0, 0
        n, s, e, w = False, False, True, False
        for i in range(len(matrix) * len(matrix[0])):

            res.append(matrix[x][y])

            if n:
                x -= 1
                if x == top:
                    n = False
                    e = True
                    left += 1
            elif s:
                x += 1
                if x == bottom:
                    s = False
                    w = True
                    right -= 1
            elif e:
                y += 1
                if y == right:
                    e = False
                    s = True
                    top += 1
            elif w:
                y -= 1
                if y == left:
                    w = False
                    n = True
                    bottom -= 1

        return res
