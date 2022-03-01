from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRECTION = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m = len(board)
        n = len(board[0])
        newBoard = [row[:] for row in board]
        for i in range(m):
            for j in range(n):
                liveCells = 0
                for direction in DIRECTION:
                    newI, newJ = i + direction[0], j + direction[1]
                    if newI < 0 or newI >= m or newJ < 0 or newJ >= n:
                        continue
                    if board[newI][newJ] == 1:
                        liveCells += 1

                if board[i][j] == 1:
                    if liveCells < 2 or liveCells > 3:
                        newBoard[i][j] = 0
                else:  # board[i][j] == 0
                    if liveCells == 3:
                        newBoard[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = newBoard[i][j]
