from typing import List


class Solution:
    """
    0 0 1 0
    0 1 1 0
    0 1 0 0

    0 0 0
    1 1 0
    0 1 1
    0 0 0
    """

    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        image = [[int(r) for r in row] for row in image]
        m, n = len(image), len(image[0])
        rowSum = [sum(row) for row in image]
        rotatedImage = self.clockwiseRotate(image)
        colSum = [sum(row) for row in rotatedImage]
        topMost = self.binarySearch(0, x, m - 1, rowSum, min)
        bottomMost = self.binarySearch(x, m - 1, 0, rowSum, max)
        leftMost = self.binarySearch(0, y, n - 1, colSum, min)
        rightMost = self.binarySearch(y, n - 1, 0, colSum, max)

        return (rightMost - leftMost + 1) * (bottomMost - topMost + 1)

    def clockwiseRotate(self, matrix):
        return list(list(x)[::-1] for x in zip(*matrix))

    def binarySearch(self, left, right, initialValue, targetSum, func):
        answer = initialValue
        while left <= right:
            mid = (left + right) // 2
            if targetSum[mid] > 0:
                if func == min:
                    answer = min(answer, mid)
                    right = mid - 1
                else:
                    answer = max(answer, mid)
                    left = mid + 1
            else:
                if func == min:
                    left = mid + 1
                else:
                    right = mid - 1

        return answer
