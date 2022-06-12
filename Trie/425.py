from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.wordSet = set()
        self.isLast = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
            node.wordSet.add(word)
        node.isLast = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return None
        return node

    def wordSetStartsWith(self, prefix):
        node = self.search(prefix)
        return [] if not node else node.wordSet


class Solution:

    def word_squares(self, words: List[str]) -> List[List[str]]:
        l = len(words[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        squares = []

        def findWordSquares(square, squares):
            ls = len(square)
            if ls == l:
                squares.append([word for word in square])
                return
            prefix = "".join([word[ls] for word in square])
            wordSet = trie.wordSetStartsWith(prefix)
            for word in wordSet:
                findWordSquares(square + [word], squares)

        for word in words:
            findWordSquares([word], squares)
        return squares
