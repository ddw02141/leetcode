from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        def dfs(ss, m):
            if ss in m:
                return m[ss]

            if not ss:
                return [""]
            res = []
            for i in range(1, len(ss) + 1):
                if ss[:i] in wordSet:
                    for word in dfs(ss[i:], m):
                        if word:
                            res.append(ss[:i] + " " + word)
                        else:
                            res.append(ss[:i])
            m[ss] = res
            return res

        return dfs(s, dict())
