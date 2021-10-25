class Solution:
    def minSteps(self, n: int) -> int:
        # A -> 0
        # AA -> 1 + 1 = 2
        # AAA -> 1 + 1 + 1 = 3
        # AAAA -> 1 + 1 + 1 + 1 = 4
        # AAAAA -> 5
        # AAAAAA -> 4
        # AAAAAAA -> 7
        # A * 8 -> 6
        # A * 10 -> 5 + 2 = 7
        # 최대한 홀수로 쪼갠 후 마지막 홀수 + 2 * (2의 승수)
        exponent = 0
        while n % 2 == 0:
            n //= 2
            exponent += 1
        if n == 1:
            return (n - 1) + 2 * exponent
        return n + 2 * exponent
