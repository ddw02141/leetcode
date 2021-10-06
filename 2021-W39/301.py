from typing import List
from itertools import combinations


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = s.count('(')
        right = s.count(')')
        answers = set()
        indicesWithLeft = [i for i, x in enumerate(s) if x == '(']
        indicesWithRight = [i for i, x in enumerate(s) if x == ')']
        possible_answers = set()
        if left > right:
            indicesCombi = combinations(indicesWithLeft, left - right)
            for indicies in indicesCombi:
                newS = s[:]
                for index in indicies:
                    newS = newS[:index] + " " + newS[index + 1:]
                newS = newS.replace(" ", "")
                possible_answers.add(newS)
        elif right > left:
            indicesCombi = combinations(indicesWithRight, right - left)
            for indicies in indicesCombi:
                newS = s[:]
                for index in indicies:
                    newS = newS[:index] + " " + newS[index + 1:]
                newS = newS.replace(" ", "")
                possible_answers.add(newS)
        else:  # left == right
            possible_answers.add(s)
        for ss in possible_answers:
            indicesWithLeft = [i for i, x in enumerate(ss) if x == '(']
            indicesWithRight = [i for i, x in enumerate(ss) if x == ')']
            for i in range(len(ss) // 2):
                indicesCombiLeft = list(combinations(indicesWithLeft, i))
                indicesCombiRight = list(combinations(indicesWithRight, i))
                for indiciesL in indicesCombiLeft:
                    newS = ss[:]
                    for indexL in indiciesL:
                        newS = newS[:indexL] + " " + newS[indexL + 1:]
                    for indiciesR in indicesCombiRight:
                        newNewS = newS[:]
                        for indexR in indiciesR:
                            newNewS = newNewS[:indexR] + " " + newNewS[indexR + 1:]
                        newNewS = newNewS.replace(" ", "")
                        if newNewS and self.isValid(newNewS):
                            answers.add(newNewS)
        if self.isValid(s):
            answers.add(s)
        if not answers:
            return [s.replace("(", "").replace(")", "")]
        maxLen = max(len(answer) for answer in answers)
        return [answer for answer in answers if len(answer) == maxLen]

    def isValid(self, s):
        stack = list()
        for ss in s:
            if ss == "(":
                stack.append("(")
            elif ss == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack = stack[:-1]
        if stack:
            return False
        return True
