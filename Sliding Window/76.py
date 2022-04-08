# https://leetcode.com/problems/minimum-window-substring/
"""
ADOBECODEBANC ABC

ADOBEC
   BECODEB
     CODEBA
         BANC
"""
from collections import defaultdict, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # tMap = {c: t.count(c) for c in set(t)}
        tMap = defaultdict(int)
        for c in t:
            tMap[c] += 1
        currentMap = defaultdict(int)
        currentIndicies = deque()
        lenAnswer = float("inf")
        answer = ""

        for i, c in enumerate(s):
            if c in tMap:
                # if currentMap[c] == tMap[c] and s[currentIndicies[0]] == c:
                #     currentIndicies.popleft()
                currentMap[c] += 1
                currentIndicies.append(i)
                # print("currentMap before", currentMap)
                while currentMap[s[currentIndicies[0]]] > tMap[s[currentIndicies[0]]]:
                    idx = currentIndicies.popleft()
                    currentMap[s[idx]] -= 1
                # print("currentMap after", currentMap)
                lenSubString = currentIndicies[-1] - currentIndicies[0] + 1
                # print("i:", i, "c:", c)
                # print(currentIndicies)
                # print(lenSubString, lenAnswer)
                if self.isWindowSubstring(currentMap, tMap):
                    if lenSubString < lenAnswer:
                        answer = s[currentIndicies[0]:currentIndicies[-1] + 1]
                        lenAnswer = len(answer)
                    firstIdx = currentIndicies.popleft()
                    currentMap[s[firstIdx]] -= 1
        return answer

    def isWindowSubstring(self, currentMap, tMap):
        for key in tMap.keys():
            if currentMap[key] < tMap[key]:
                return False

        return True
