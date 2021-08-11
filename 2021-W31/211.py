import collections


class TrieNode:

    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.child[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not node:
            return
        if not word:
            self.res = self.res or node.isWord
            return
        w = word[0]
        if w == ".":
            for child in node.child.values():
                self.dfs(child, word[1:])
        else:
            self.dfs(node.child.get(w), word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
