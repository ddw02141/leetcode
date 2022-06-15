class Solution:
    def __init__(self):
        self.answer = 0

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words.sort(key=len)
        for word in words:
            dp[word] = max(dp.get(word[:i] + word[i + 1:], 0) for i in range(len(word))) + 1

        return max(dp.values())
