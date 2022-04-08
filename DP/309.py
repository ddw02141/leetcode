from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0 for _ in range(n)]
        notHold = [0 for _ in range(n)]
        sell = [False for _ in range(n)]
        hold[0] = -prices[0]
        for i in range(1, n):
            if notHold[i - 1] < hold[i - 1] + prices[i]:
                notHold[i] = hold[i - 1] + prices[i]
                sell[i] = True
            else:
                notHold[i] = notHold[i - 1]

            hold[i] = max(hold[i - 1], -prices[i])
            if not sell[i - 1]:
                hold[i] = max(hold[i], notHold[i - 1] - prices[i])
            if i > 2:
                hold[i] = max(hold[i], notHold[i - 2] - prices[i])

        # print(hold)
        # print(notHold)

        return notHold[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))  # Expect 3
    print(solution.maxProfit([1, 4, 2]))  # Expect 3
    print(solution.maxProfit([2, 4, 1, 7]))  # Expect 6
