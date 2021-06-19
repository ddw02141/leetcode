# https://leetcode.com/problems/odd-even-jump/
# arr.length <= 2 * 10^4

class Solution:
    def oddJump(self, arr, target):
        left = 0
        right = len(arr) - 1
        # 1. 숫자 min 2. index min
        ans = float("inf")
        ansIdx = float("inf")
        while left <= right:
            mid = (left + right) // 2
            # print("left:", left, "mid:", mid,"right:",right)
            if arr[mid][0] >= target[0]:
                if ans == arr[mid][0]:
                    ansIdx = min(ansIdx, arr[mid][1])
                elif ans > arr[mid][0]:
                    ans = arr[mid][0]
                    ansIdx = arr[mid][1]
                right = mid - 1
            else:
                left = mid + 1
        return ansIdx

    def evenJump(self, arr, target):
        left = 0
        right = len(arr) - 1
        ans = float("-inf")
        ansIdx = float("inf")
        # 1. 숫자 max 2. index min
        while left <= right:
            mid = (left + right) // 2
            # print("left:", left, "mid:", mid,"right:",right)
            if arr[mid][0] <= target[0]:
                if ans == arr[mid][0]:
                    ansIdx = min(ansIdx, arr[mid][1])
                elif ans < arr[mid][0]:
                    ans = arr[mid][0]
                    ansIdx = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ansIdx

    def oddEvenJumps(self, arr: List[int]) -> int:
        # [10,13,12,14,15]
        # [(10, 0),(12,2),(13,1),(14,3),(15,4)]
        answer = 0
        for i, a in enumerate(arr):
            # print("i:", i)
            trial = 1
            newA = (a, i)
            idx = i
            while idx < len(arr) - 1:
                newArr = [(b, j + idx + 1) for j, b in enumerate(arr[idx + 1:])]
                # newArr.sort(key=lambda x:(x[0], -x[1]))

                # print("newA:", newA)
                if trial % 2 == 1:
                    newArr.sort()
                    # print("newArr:", newArr)
                    idx = self.oddJump(newArr, newA)
                    # print("oddJump result:", idx)
                    if idx == float("inf"):
                        break
                    newA = (arr[idx], idx)
                else:
                    newArr.sort(key=lambda x: (x[0], -x[1]))
                    # print("newArr:", newArr)
                    idx = self.evenJump(newArr, newA)
                    # print("evenJump result:", idx)
                    if idx == float("inf"):
                        break
                    newA = (arr[idx], idx)
                trial += 1
            # print("final newA:", newA)
            if idx == len(arr) - 1:
                # print("i:", i,"answer++!")
                answer += 1
        return answer