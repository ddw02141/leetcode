from typing import List

from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0 for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1
        q = deque([node for node in range(n) if degree[node] == 1])
        remainingNodes = n
        while remainingNodes > 2:
            remainingNodes -= len(q)
            newQ = deque([])
            for node in q:
                for child in adj[node]:
                    degree[child] -= 1
                    if degree[child] == 1:
                        newQ.append(child)
            q = newQ

        return list(q)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))  # Expect [3,4]
    print(solution.findMinHeightTrees(5, [[0, 1], [0, 2], [0, 3], [3, 4]]))  # Expect [0,3]
    print(solution.findMinHeightTrees(1, []))  # Expect [0]
