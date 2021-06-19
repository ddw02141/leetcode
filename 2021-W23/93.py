# https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def backtrack(temp, ss):
            if len(temp) == 4:
                if not ss:
                    answer.append(".".join(temp))
                return
            for i in range(1, min(3, len(ss)) + 1):
                if i != 1 and ss[0] == '0':
                    continue
                part = ss[:i]
                if int(part) > 255:
                    continue
                backtrack(temp + [part], ss[i:])

        backtrack([], s)
        return answer
