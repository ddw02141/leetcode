from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window => 1로 바뀌는 0의 위치는 항상 연속적임(1이 없다고 생각했을 때)
        answer = 0
        zeros = 0
        current = list()
        for num in nums:
            if num == 1:
                current.append(num)
            else:
                if zeros == k:
                    answer = max(answer, len(current))
                    if 0 in current:
                        current = current[current.index(0) + 1:]
                        zeros -= 1
                    else:
                        current = list()
                if zeros < k:
                    zeros += 1
                    current.append(num)
        answer = max(answer, len(current))
        return answer


if __name__ == "__main__":
    solution = Solution()

    print("------------------ Test Case 1 ------------------")
    sol = solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    ans = 6
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution.longestOnes([0, 0, 1, 1, 1, 0, 0], 0)
    ans = 3
    assert ans == sol, f"Expected {ans} Actual {sol}"
