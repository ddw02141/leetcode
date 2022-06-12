from typing import List
from collections import defaultdict


class Solution:

    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        wordToAbbreviation = defaultdict(str)
        abbreviationCounts = defaultdict(int)
        prefixLenghts = defaultdict(lambda: 1)

        for word in words:
            abb = self.getAbbreviation(word, 1)
            wordToAbbreviation[word] = abb
            abbreviationCounts[abb] += 1

        while True:
            unique = True
            for i, word in enumerate(words):
                abb = wordToAbbreviation[word]
                if abbreviationCounts[abb] > 1:
                    # abbreviationCounts[abb] -= 1
                    prefixLenghts[i] += 1
                    newAbb = self.getAbbreviation(word, prefixLenghts[i])
                    wordToAbbreviation[word] = newAbb
                    abbreviationCounts[newAbb] += 1
                    unique = False
            if unique:
                break

        return [wordToAbbreviation[word] for word in words]

    def getAbbreviation(self, word, prefixLen):
        if prefixLen >= len(word) - 2:
            return word

        return word[:prefixLen] + str(len(word) - prefixLen - 1) + word[-1]
