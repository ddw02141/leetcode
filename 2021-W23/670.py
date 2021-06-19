# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        # 가능한 한 왼쪽에 있는 수와
        # 가장 큰 수, 값이 같다면 가능한 한 오른쪽에 있는 수를 바꾸어 줘야 함
        # 8899 => 9898
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    A[i], A[last.get(d)] = A[last.get(d)], A[i]
                    return int("".join(map(str, A)))

        return num
