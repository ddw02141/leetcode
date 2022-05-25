from typing import List
from bisect import bisect_right


def getRank(matrix, num):
    return sum(bisect_right(row, num) for row in matrix)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = - 10 ** 9
        right = 10 ** 9
        answer = 10 ** 9
        while left <= right:
            mid = left + (right - left) // 2
            rank = getRank(matrix, mid)
            if rank >= k:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([[-5]], 1))
    print(solution.kthSmallest([[1, 2], [1, 3]], 4))
    print(solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
