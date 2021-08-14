class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = i번째 집까지 털었을 때 최대로 털 수 있는 금액
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], dp[0])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
