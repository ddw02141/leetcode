# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        l = [s.count(c) for c in set(s)]
        l.sort(reverse=True)

        answer = 0
        cs = set()
        for ll in l:
            while ll in cs and ll > 0:
                ll -= 1
                answer += 1
            cs.add(ll)
        return answer
