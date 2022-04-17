from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [(root, 0, 0)]
        yDict = defaultdict(list)
        maxY, minY = 0, 0
        while q:
            node, x, y = q.pop(0)
            yDict[y].append(node.val)
            if node.left:
                newX, newY = x + 1, y - 1
                minY = min(minY, y - 1)
                q.append((node.left, newX, newY))
            if node.right:
                newX, newY = x + 1, y + 1
                maxY = max(maxY, y + 1)
                q.append((node.right, newX, newY))
        # print(minY, maxY)
        # print(yDict)
        answer = []
        for y in range(minY, maxY + 1):
            answer.append(yDict[y])

        return answer
