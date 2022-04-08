# https://leetcode.com/problems/super-ugly-number/
"""
12
[2,7,13,19]
[1,1, 1, 1]

[1]
[2,7,13,19] -> 1
[4,7,13,19] -> 2
[7,8,13,19] -> 4
[8,14,49,13,19] -> 7


"""
from typing import List
from heapq import heappop, heappush


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        while n > 0:
            smallest = heappop(ugly)
            for prime in primes:
                heappush(ugly, smallest * prime)
                if smallest % prime == 0:
                    break
            n -= 1

        return smallest
