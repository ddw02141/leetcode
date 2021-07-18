# https://leetcode.com/problems/palindrome-pairs/

class TrieNode:
    def __init__(self):
        self.index = -1
        self.next = dict()
        self.remainStrPalIndexes = list()

    def __str__(self):
        return "index: " + str(self.index) + " self.next: " + str(self.next.keys()) + " remainStrPalIndexes: " + str(
            self.remainStrPalIndexes)

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answer = list()
        root = TrieNode()

        for i, word in enumerate(words):
            self.createTrie(i, word, root)
        for i, word in enumerate(words):
            self.search(i, word, root, answer)

        return answer

    def createTrie(self, i, word, root):
        wordR = word[::-1]
        cur = root
        for j, w in enumerate(wordR):
            if w not in cur.next:
                cur.next[w] = TrieNode()
            if wordR[j:] == wordR[j:][::-1]:
                cur.remainStrPalIndexes.append(i)
            cur = cur.next[w]
        cur.index = i
        cur.remainStrPalIndexes.append(i)

    def search(self, i, word, root, ans):
        cur = root
        for j, w in enumerate(word):
            if cur.index >= 0 and cur.index != i and word[j:] == word[j:][::-1]:
                ans.append([i, cur.index])
            if w not in cur.next:
                return
            cur = cur.next[w]
        if cur and cur.remainStrPalIndexes:
            ans.extend([i, k] for k in cur.remainStrPalIndexes if k != i)
