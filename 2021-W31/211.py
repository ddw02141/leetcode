class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = [{}, False]

    def addWord(self, word: str) -> None:
        trie = self.trie
        words = [""]
        for w in word:
            words = [existing + wOrDot for wOrDot in (w, ".") for existing in words]
        for Word in words:
            trie = self.trie
            for i, w in enumerate(Word):
                if w not in trie[0]:
                    trie[0][w] = [{}, False]
                trie[0][w][1] = trie[0][w][1] or (i == len(Word) - 1)
                trie = trie[0][w]

    def search(self, word: str) -> bool:
        trie = self.trie
        for w in word:
            if w not in trie[0]:
                return False
            trie = trie[0][w]
        return trie[1]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
