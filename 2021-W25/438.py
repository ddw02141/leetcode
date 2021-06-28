class Solution:
    characters = [chr(ord('a') + i) for i in range(26)]

    def isAnagram(self, subSCounts, pCounts):
        for c in self.characters:
            if subSCounts[c] != pCounts[c]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        pCounts, subSCounts = {c: 0 for c in self.characters}, {c: 0 for c in self.characters}
        for i in set(p):
            pCounts[i] = p.count(i)
        for i in range(min(len(p), len(s))):
            subSCounts[s[i]] += 1
        for i in range(len(s) - len(p) + 1):
            if self.isAnagram(subSCounts, pCounts):
                answer.append(i)
            subSCounts[s[i]] -= 1
            if i + len(p) < len(s):
                subSCounts[s[i + len(p)]] += 1
        return answer
