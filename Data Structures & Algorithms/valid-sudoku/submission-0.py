class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            current = [0] * 10
            for i in row:
                if i != ".":
                    if current[int(i)] == 0:
                        current[int(i)] = 1
                    else:
                        print("HERE2")
                        print(i)
                        return False

        # Check Cols
        for j in range(9):
            current = [0] * 10
            for i in board[j]:
                if i != ".":
                    if current[int(i)] == 0:
                        current[int(i)] = 1
                    else:
                        print("HERE1")
                        print(i)
                        return False
        
        # Check squares
        # How can we iterate through squares
        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

        # have start coord
        # increment x by 3 twice
        # then back to zero and then increment y by 3
        # do this three times

        # iterate through smaller square

        def iterate_small(origin_x, origin_y):
            current = [0] * 10
            for i in range(3):
                origin_x += i
                for j in range(3):
                    origin_y += j
                    if board[i][j] != ".":
                        if current[int(board[i][j])] == 0:
                            current[int(board[i][j])] = 1
                        else:
                            print("HERE")
                            print(board[i][j])
                            return False
            return True
        
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                if not iterate_small(x, y):
                    return False
        
        return True


