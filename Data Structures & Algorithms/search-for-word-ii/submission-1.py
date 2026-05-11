class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:


        # for each letter in the board check if it's in any of the words
        # O(m*n*k) m*n = board, k = number of words
        # if it is in the word, check 


        # for each word, get the starting letter and find every instance of that letter in the board
        # go to every instance and DFS through it, checking if you can make the string from that
        # letter as the starting point
        # O(m^2.n^2.k)

        res = []

        for word in words:
            c = word[0]

            positions = []

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == c:
                        positions.append((i,j))

            for position in positions:
                def dfs(position, target, index, seen):
                    i,j = position

                    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or seen[i][j]:
                        return False

                    if board[i][j] == target[index]:
                        if len(target) == index + 1:
                            return True

                        new_positions = [
                            (i + 1, j),
                            (i - 1, j),
                            (i, j + 1),
                            (i, j - 1),
                        ]

                        seen[i][j] = True

                        for new_position in new_positions:
                            if dfs(new_position, target, index + 1, seen):
                                return True
                        seen[i][j] = False
                        return False
                    else:
                        return False

                seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if dfs(position, word, 0, seen):
                    res.append(word)
                    break
        
        return res


