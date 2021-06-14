# https://leetcode.com/problems/expression-add-operators/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # use cur, prev
        # 3 + 456*2 => 3 + 456 * 23
        # backtrack(5, 915, 912, 3+456*2)
        # backtrack(6, 3 + 912*10 + 3, 912*10 + 3)
        def backtrack(idx, cur, prev, resultStr):
            if idx == len(num):
                if cur == target:
                    answer.append(resultStr)
                return
            for j in range(1, len(num) - idx + 1):
                if num[idx] == '0' and j > 1:
                    break
                s = num[idx:idx + j]
                n = int(num[idx:idx + j])
                if idx == 0:
                    # For first number
                    backtrack(idx + j, cur + n, n, resultStr + s)
                else:
                    backtrack(idx + j, cur + n, n, resultStr + "+" + s)
                    backtrack(idx + j, cur - n, -n, resultStr + "-" + s)
                    backtrack(idx + j, cur - prev + prev * n, prev * n, resultStr + "*" + s)

        answer = []
        backtrack(0, 0, 0, "")
        return answer
