from typing import List
from heapq import heappop, heappush


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.wordPq = list()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            heappush(cur.wordPq, word)
            cur = cur.children[w]
        heappush(cur.wordPq, word)

    def search(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                return []
            cur = cur.children[w]
        recommendation = []
        recommendationCnt = 3
        while cur.wordPq and recommendationCnt > 0:
            recommendation.append(heappop(cur.wordPq))
            recommendationCnt -= 1

        return recommendation


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.add(product)

        recommendations = []
        for i in range(len(searchWord)):
            recommendation = trie.search(searchWord[:i + 1])
            recommendations.append(recommendation)

        return recommendations
