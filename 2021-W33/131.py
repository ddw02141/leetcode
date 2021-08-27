# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.backtrack(s, 0, [], answer)
        return answer

    def backtrack(self, s, idx, current, answer):
        if idx == len(s):
            answer.append(current)
            return
        for i in range(1, len(s) - idx + 1):
            if s[idx:idx + i] == s[idx:idx + i][::-1]:
                self.backtrack(s, idx + i, current + [s[idx:idx + i]], answer)
