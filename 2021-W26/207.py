# https://leetcode.com/problems/course-schedule/
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for d, s in prerequisites:
            if d == s:
                return False
            m[s].append(d)

        def isCyclic(node, visited, recStack):
            visited[node] = True
            recStack[node] = True
            for d in m[node]:
                if not visited[d]:
                    if isCyclic(d, visited, recStack):
                        return True
                elif recStack[d]:
                    return True
            recStack[node] = False
            return False

        visited = [False for _ in range(numCourses)]
        recStack = [False for _ in range(numCourses)]
        for start in range(numCourses):
            if isCyclic(start, visited, recStack):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
    print(solution.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
