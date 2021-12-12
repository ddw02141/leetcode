from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = -1, -1
        answer = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    answer += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    answer += rmax - height[r]
                r -= 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
