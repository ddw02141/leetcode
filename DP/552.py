class Solution:
    def checkRecord(self, n: int) -> int:
        if n <= 3:
            return [None, 3, 8, 19][n]
        MODULO = 10 ** 9 + 7
        withoutA = [0 for _ in range(n + 1)]
        withoutA[1] = 2
        withoutA[2] = 4
        withoutA[3] = 7
        for i in range(4, n + 1):
            # XXXX = PXXX + LPXX + LLPX
            withoutA[i] = (withoutA[i - 1] + withoutA[i - 2] + withoutA[i - 3]) % MODULO
        answer = withoutA[n]
        for i in range(n):
            # i: A's position(0 ~ n - 1)
            if i == 0 or i == n - 1:
                answer += withoutA[n - 1]
            else:
                answer += (withoutA[i] * withoutA[n - i - 1])
            answer %= MODULO

        return answer
