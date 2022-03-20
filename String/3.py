class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        cSet = dict()
        start = 0
        for i, ss in enumerate(s):
            if ss not in cSet:
                cSet[ss] = i
            else:
                answer = max(answer, i - start)
                if cSet[ss] + 1 > start:
                    start = cSet[ss] + 1
                cSet[ss] = i
        #     print("i:", i, "ss:",ss, "cSet:", cSet, "start:", start, "answer:", answer)
        # print("len(s) - start:", len(s) - start)
        return max(answer, len(s) - start)
