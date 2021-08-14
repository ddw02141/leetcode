class Solution:
    def __init__(self):
        self.dp = []

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        self.nums = nums
        self.dp = [None for _ in range(n)]
        return self.canJumpBack(n - 1)

    def canJumpBack(self, idx):
        if idx == 0:
            return True
        if self.dp[idx] != None:
            return self.dp[idx]
        result = False
        for i in range(idx)[::-1]:
            if result:
                return True
            if self.nums[i] >= idx - i:
                result = result or self.canJumpBack(i)
        self.dp[idx] = result
        return result
