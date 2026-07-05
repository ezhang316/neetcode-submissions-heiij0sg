class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        if n < 4:
            return []
        
        res = []

        cols = [0 for _ in range(n)]
        diags_l = [0 for _ in range(2 * n - 1)]
        diags_r = [0 for _ in range(2 * n - 1)]

        print_2D_grid = [["." for _ in range(n)] for _ in range(n)]

        def rec(row, prev_q_col):
            if row >= n:
                new_list = []
                for i in range(n):
                    new_list.append("".join(print_2D_grid[i]))
                res.append(new_list)
                return

            for i in range(n):
                if cols[i] != 0:
                    continue
                if i <= prev_q_col + 1 and i >= prev_q_col - 1:
                    continue
                l_diag = n - row + i -1
                r_diag = 2*n - 1 - row - i -1
                if diags_l[l_diag] != 0 or diags_r[r_diag] != 0:
                    continue
                
                cols[i] = 1
                diags_l[l_diag] = 1
                diags_r[r_diag] = 1
                print_2D_grid[row][i] = "Q"

                rec(row + 1, i)

                cols[i] = 0
                diags_l[l_diag] = 0
                diags_r[r_diag] = 0
                print_2D_grid[row][i] = "."

        rec(0, -2)
        return res

                

        
