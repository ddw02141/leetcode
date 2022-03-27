"""
[3,0,1,4,2],
[5,6,3,2,1],
[1,2,0,1,5],
[4,1,0,1,7],
[1,0,3,0,5]
"""


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.tree = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        if diff == 0:
            return
        self.matrix[row][col] = val
        x = row + 1
        while x <= self.m:
            y = col + 1
            while y <= self.n:
                self.tree[x][y] += diff
                y += (y & -y)
            x += (x & -x)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sumRegionFromOrigin(r2, c2) - self.sumRegionFromOrigin(r2, c1 - 1) \
               - self.sumRegionFromOrigin(r1 - 1, c2) + self.sumRegionFromOrigin(r1 - 1, c1 - 1)

    def sumRegionFromOrigin(self, r, c):
        ps = 0
        x = r
        while x > 0:
            y = c
            while y > 0:
                ps += self.tree[x][y]
                y -= (y & -y)
            x -= (x & -x)

        return ps

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
