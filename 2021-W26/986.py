# https://leetcode.com/problems/interval-list-intersections/


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstIdx = 0
        secondIdx = 0
        answer = []
        while firstIdx < len(firstList) and secondIdx < len(secondList):
            fs, fe = firstList[firstIdx]
            ss, se = secondList[secondIdx]
            intersection = [max(fs,ss), min(fe,se)]
            if intersection[0] <= intersection[1]:
                answer.append(intersection)
            if fe <= se:
                firstIdx += 1
            else:
                secondIdx += 1
        return answer
