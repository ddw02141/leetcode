from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = list()
        visited = [0 for _ in range(len(graph))]
        for i, g in enumerate(graph):
            if g and visited[i] == 0:
                visited[i] = 1
                q = [i]
                while q:
                    parent = q.pop(0)
                    for child in graph[parent]:
                        if visited[child] == 0:
                            visited[child] = 2 if visited[parent] == 1 else 1
                            q.append(child)
                        else:
                            if visited[parent] == visited[child]:
                                return False

        return True
