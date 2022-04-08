from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rest = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        sell = [0 for _ in range(n)]
        buy[0] = -prices[0]

        for i in range(1, n):
            rest[i] = max(rest[i - 1], sell[i - 1])
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]

        return max(rest[-1], buy[-1], sell[-1])
