class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
          s e a
        e 0 1 1
        a 0 1 2
        t 0 1 2

          l e e t c o d e
        e 0 1 1 1 1 1 1 1
        t 0 1 1 2 2 2 2 2
        c 0 1 1 1 3 3 3 3
        o 0 1 1 1 3 4 4 4
        len("leetcode") + len("etco") - 4 * 2 = 4
          m o n e y
        f 0 0 0 0 0
        o 0 1 1 1 1
        o 0 1 1 1 1
        d 0 1 1 1 1

          m o o n e y
        f 0 0 0 0 0 0
        o 0 1 1 1 1 1
        o 0 1 2
        d
        """
        m, n = len(word1), len(word2)
        matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                if word1[i - 1] == word2[j - 1]:
                    matrix[i][j] = max(matrix[i][j], matrix[i - 1][j - 1] + 1)

        return m + n - 2 * matrix[m][n]
