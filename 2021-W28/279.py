# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        q, newQ, answer = {n}, set(), 1
        while q:
            for num in q:
                for square in squares:
                    if num == square:
                        return answer
                    newQ.add(num - square)
            q, newQ, answer = newQ, set(), answer + 1
