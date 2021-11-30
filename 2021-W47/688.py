import collections


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        possible_direction = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        possiblity_out = 0
        possibility_of_each_move = 1
        q = collections.defaultdict(int)
        q[(row, column)] = 1
        for _ in range(k):
            possibility_of_each_move /= 8
            new_q = collections.defaultdict(int)
            for row_col, count in q.items():
                row, col = row_col
                for x, y in possible_direction:
                    new_x = row + x
                    new_y = col + y
                    if 0 <= new_x < n and 0 <= new_y < n:
                        new_q[(new_x, new_y)] += count
                    else:
                        possiblity_out += (possibility_of_each_move * count)
            q = new_q
        return 1 - possiblity_out
