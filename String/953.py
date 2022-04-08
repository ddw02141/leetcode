from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            for i in range(len(w1)):
                if i >= len(w2):
                    return False

                if orderMap[w1[i]] == orderMap[w2[i]]:
                    continue
                elif orderMap[w1[i]] <= orderMap[w2[i]]:
                    break
                else:
                    return False

        return True
