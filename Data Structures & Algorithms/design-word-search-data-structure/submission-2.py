class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:

    def __init__(self):
        self.d = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.d
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def search(i: int, d) -> bool:
            if i >= len(word):
                return d.word

            if word[i] in d.children:
                return search(i + 1, d.children[word[i]])

            if word[i] == ".":
                for child in d.children.values():
                    if search(i + 1, child):
                        return True

            return False

        return search(0, self.d)

        

