class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

    def search(self, word: str) -> bool:
        def search(i: int, d: dict) -> bool:
            if i >= len(word) and not d:
                return True
            elif i >= len(word):
                return False
            
            if word[i] in d:
                return search(i + 1, d[word[i]])
            elif word[i] == ".":
                for value in d.values():
                    if search(i + 1, value):
                        return True
            else:
                return False
        cur = self.d
        for i in range(len(word)):
            if word[i] not in cur and word[i] != ".":
                return False
            
            if word[i] in cur:
                cur = cur[word[i]]
                continue
            
            if word[i] == ".":
                for d in cur.values():
                    if search(i + 1, d):
                        return True
                return False
        return True

        

