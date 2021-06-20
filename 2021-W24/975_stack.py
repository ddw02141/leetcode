# https://leetcode.com/problems/odd-even-jump/
# [2, 3, 1, 1, 4]
# [(1,2), (1,3), (2,0), (3,1), (4,4)]
# [2]
# [3] & nextHigher[2] = 3
# [3, 0]
# [3] & nextHigher[0] = 1
# [3, 1]
# [3] & nextHigher[1] = 4
# [] & nextHigher[3] = 4

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # nextHigher[i] = j : i에서 oddJump -> j
        # nextLower[i] = j: i에서 evenJump -> j
        nextHigher, nextLower = [None for _ in range(n)], [None for _ in range(n)]

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nextLower[stack.pop()] = i
            stack.append(i)

        higher, lower = [False for _ in range(n)], [False for _ in range(n)]
        higher[-1] = lower[-1] = True
        for i in range(n - 2, -1, -1):
            if nextHigher[i]:
                higher[i] = lower[nextHigher[i]]
            if nextLower[i]:
                lower[i] = higher[nextLower[i]]
        return sum(int(val) for val in higher)
