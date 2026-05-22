class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = []

        def dfs(x,y,i):
            if (x,y) in seen:
                return False
            
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False

            if board[x][y] != word[i]:
                return False
            
            if i + 1 == len(word):
                return True

            seen.append((x,y))

            res1 = dfs(x + 1, y, i + 1)
            res2 = dfs(x - 1, y, i + 1)
            res3 = dfs(x, y + 1, i + 1)
            res4 = dfs(x, y - 1, i + 1)

            seen.pop()

            return res1 or res2 or res3 or res4
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x,y,0):
                    return True
        return False
