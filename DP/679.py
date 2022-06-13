class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        All possible order: 4! = 24
        dp스멜이 나는데, 뭘 어떻게 시작할지 전혀 감이 안오네
        dp[0:4]
        dp[0:1] + dp[1:4]
        dp[0:1] - dp[1:4]
        dp[0:1] * dp[1:4]
        dp[0:1] / dp[1:4]

        dp[0:1] ? dp[1:4]
        dp[0:2] ? dp[2:4]
        dp[0:3] ? dp[3:4]

        """
        shuffledDecks = self.shuffle(cards)
        for shuffledDeck in shuffledDecks:
            dp = [[set() for _ in range(5)] for _ in range(4)]
            for i, card in enumerate(shuffledDeck):
                dp[i][1].add(card)
            for i in range(3):
                for left in dp[i][1]:
                    for right in dp[i + 1][1]:
                        dp[i][2].add(left + right)
                        dp[i][2].add(left - right)
                        dp[i][2].add(left * right)
                        if right != 0:
                            dp[i][2].add(left / right)
            for i in range(2):
                for leftLen in range(1, 2 + 1):
                    for left in dp[i][leftLen]:
                        for right in dp[i + leftLen][3 - leftLen]:
                            dp[i][3].add(left + right)
                            dp[i][3].add(left - right)
                            dp[i][3].add(left * right)
                            if right != 0:
                                dp[i][3].add(left / right)
            for i in range(1):
                for leftLen in range(1, 3 + 1):
                    for left in dp[i][leftLen]:
                        for right in dp[i + leftLen][4 - leftLen]:
                            dp[i][4].add(left + right)
                            dp[i][4].add(left - right)
                            dp[i][4].add(left * right)
                            if right != 0:
                                dp[i][4].add(left / right)
            for num in dp[0][4]:
                if 23.9999 <= num <= 24.0001:
                    return True
        return False

    def shuffle(self, cards):
        if len(cards) == 1:
            return [cards]
        permutations = []
        for i in range(len(cards)):
            perms = self.shuffle(cards[:i] + cards[i + 1:])
            for p in perms:
                permutations.append([cards[i], *p])

        return permutations
