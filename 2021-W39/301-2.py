# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answer = list()
        self.makeAnswer(s, answer, 0, 0, ['(', ')'])
        return answer

    def makeAnswer(self, s, answer, countIdx, removeIdx, par):
        stack = 0
        for i in range(countIdx, len(s)):
            if s[i] == par[0]:
                stack += 1
            elif s[i] == par[1]:
                stack -= 1

            if stack >= 0: continue

            for j in range(removeIdx, i + 1):
                if s[j] == par[1] and (j == removeIdx or s[j - 1] != par[1]):
                    self.makeAnswer(s[:j] + s[j + 1:], answer, i, j, par)
            return

        reversedS = s[::-1]
        if par[0] == ')':
            # s is revered string already
            # so reversedS must be vaild string
            answer.append(reversedS)
        else:
            self.makeAnswer(reversedS, answer, 0, 0, par[::-1])
