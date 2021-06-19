# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    answer = 0

    def maxLength(self, arr: List[str]) -> int:
        globalCharacters = set()
        characters = [chr(ord("a") + i) for i in range(26)]
        answer = 0

        def containsDuplicatedCharacters(s):
            for i in set(s):
                if s.count(i) > 1:
                    return True
            return False

        def backtrack(idx):
            if idx == len(arr):
                self.answer = max(self.answer, len(globalCharacters))
                return
            s = arr[idx]
            if containsDuplicatedCharacters(s):
                backtrack(idx + 1)
                return
            for ss in s:
                if ss in globalCharacters:
                    backtrack(idx + 1)
                    return
            # Exclude idx
            backtrack(idx + 1)
            # Enclude idx
            for ss in s:
                globalCharacters.add(ss)
            backtrack(idx + 1)
            for ss in s:
                globalCharacters.remove(ss)

        backtrack(0)

        return self.answer