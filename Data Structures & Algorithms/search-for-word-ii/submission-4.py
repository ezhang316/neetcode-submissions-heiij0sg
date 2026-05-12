class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}       # char -> TrieNode
                self.is_end = False      # marks end of a word
                self.index = -1
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word: str, index):
                node = self.root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                node.is_end = True
                node.index = index


        t = Trie()

        for i in range(len(words)):
            t.insert(words[i], i)

        res = []

        root = t.root

        for i in range(len(board)):
            for j in range(len(board[i])):
                def dfs(position, root, seen):
                    
                    i,j = position

                    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or seen[i][j]:
                        return False

                    if board[i][j] in root.children:
                        child = root.children[board[i][j]]
                        if child.is_end and child.index not in res:
                            res.append(words[child.index])

                        new_positions = [
                            (i + 1, j),
                            (i - 1, j),
                            (i, j + 1),
                            (i, j - 1),
                        ]

                        seen[i][j] = True

                        for new_position in new_positions:
                            if dfs(new_position, child, seen):
                                return True
                        seen[i][j] = False
                        return False
                    else:
                        return False
                seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                result = dfs((i,j), root, seen)
        
        return res


    

    


