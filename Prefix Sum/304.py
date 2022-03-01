from typing import List


# 1 2 3
# 4 5 6
# 7 8 9

#  1  3  6
#  5 12 21
# 12 27 45

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.prefixSum = [[0 for _ in range(n)] for _ in range(m)]
        self.prefixSum[0][0] = matrix[0][0]
        for i in range(1, m):
            self.prefixSum[i][0] = matrix[i][0] + self.prefixSum[i - 1][0]
        for j in range(1, n):
            self.prefixSum[0][j] = matrix[0][j] + self.prefixSum[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                self.prefixSum[i][j] = self.prefixSum[i - 1][j] + self.prefixSum[i][j - 1] + matrix[i][j] - \
                                       self.prefixSum[i - 1][j - 1]
        print(self.prefixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        elif row1 == col1 == 0:
            return self.prefixSum[row2][col2]
        elif row1 == 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row2][col1 - 1]
        elif col1 == 0:
            return self.prefixSum[row2][col2] - self.prefixSum[row1 - 1][col2]
        return self.prefixSum[row2][col2] - self.prefixSum[row2][col1 - 1] - \
               self.prefixSum[row1 - 1][col2] + self.prefixSum[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
