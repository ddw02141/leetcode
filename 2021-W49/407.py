from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        answer = 0
        length = len(heightMap)
        for i, heights in enumerate(heightMap[1:-1]):
            idx = i + 1
            l, r = 0, len(heights) - 1
            lmax, rmax = -1, -1
            while l < r:
                if heights[l] < heights[r]:
                    if heights[l] > lmax:
                        lmax = heights[l]
                    elif heights[l] < lmax:
                        umax = max(heightMap[x][l] for x in range(idx))
                        dmax = max(heightMap[x][l] for x in range(idx + 1, length))
                        answer += min(lmax, umax, dmax) - heights[l]
                    l += 1
                else:
                    if heights[r] > rmax:
                        rmax = heights[r]
                    elif heights[r] < rmax:
                        umax = max(heightMap[x][r] for x in range(idx))
                        dmax = max(heightMap[x][r] for x in range(idx + 1, length))
                        answer += min(rmax, umax, dmax) - heights[r]
                    r -= 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    # print(solution.trapRainWater([[1, 4, 3, 1, 3, 2],
    #                               [3, 2, 1, 3, 2, 4],
    #                               [2, 3, 3, 2, 3, 1]]))  # Expect 4
    # print(solution.trapRainWater([[3, 3, 3, 3, 3],
    #                               [3, 2, 2, 2, 3],
    #                               [3, 2, 1, 2, 3],
    #                               [3, 2, 2, 2, 3],
    #                               [3, 3, 3, 3, 3]]))  # Expect 10
    print(solution.trapRainWater([[12, 13, 1, 12],
                                  [13, 4, 13, 12],
                                  [13, 8, 10, 12],
                                  [12, 13, 12, 12],
                                  [13, 13, 13, 13]]))  # Expect 14
