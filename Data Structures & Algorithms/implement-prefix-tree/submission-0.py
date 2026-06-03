class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i >= len(word):
                return node.word
            
            if word[i] not in node.children:
                return False
            
            return dfs(i + 1, node.children[word[i]])
        
        return dfs(0, self.root)

    def startsWith(self, prefix: str) -> bool:
        def dfs(i, node):
            if i >= len(prefix):
                return True
            
            if prefix[i] not in node.children:
                return False
            
            return dfs(i + 1, node.children[prefix[i]])
        
        return dfs(0, self.root)
        
        