# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        answer = 0
        for i, word in enumerate(words):
            charSet = set(w for w in word)
            maxLen = 0
            for targetWord in words[i:]:
                impossible = False
                for c in charSet:
                    if c in targetWord:
                        impossible = True
                        break
                if impossible:
                    continue
                maxLen = max(maxLen, len(targetWord))
            answer = max(answer, len(word) * maxLen)
        return answer
