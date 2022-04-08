# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        answer = 0
        mostFrequentCharacterCount = 0
        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            mostFrequentCharacterCount = max(mostFrequentCharacterCount, counts[s[right]])
            lettersToChangeCount = right - left + 1 - mostFrequentCharacterCount
            if lettersToChangeCount > k:
                counts[s[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)

        return answer
