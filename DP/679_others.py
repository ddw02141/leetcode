class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs([card for card in cards])

    def dfs(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                excludeIJ = [card for k, card in enumerate(cards) if k != i and k != j]
                for result in self.op(cards[i], cards[j]):
                    newCards = excludeIJ[:] + [result]
                    if self.dfs(newCards):
                        return True

        return False

    def op(self, n1, n2):
        results = []
        results.append(n1 + n2)
        results.append(n1 - n2)
        results.append(n2 - n1)
        results.append(n1 * n2)
        if n1 != 0:
            results.append(n2 / n1)
        if n2 != 0:
            results.append(n1 / n2)
        return results
