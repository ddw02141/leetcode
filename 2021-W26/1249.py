# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removeIdxs = list()
        stack = list()
        for i, ss in enumerate(s):
            if ss == "(":
                stack.append(i)
            elif ss == ")":
                if not stack:
                    removeIdxs.append(i)
                else:
                    del stack[-1]
        removeIdxs += stack
        return "".join(ss for i, ss in enumerate(s) if i not in removeIdxs)
