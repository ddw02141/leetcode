from typing import List


class Node:
    def __init__(self, val, isRoot=False):
        self.val = val
        self.childs = set()
        self.isRoot = isRoot

    def __str__(self):
        return "val: " + self.val + " child: [" + ",".join(child.val for child in self.childs) + "] isRoot: " + str(
            self.isRoot)


class Solution:

    def getIdx(self, c):
        return ord(c) - ord('a')

    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        # nodes[0] = Node('a') if 'a' appears in words!
        nodes = [None for _ in range(26)]
        queue = list()
        queue.append(words)
        while queue:
            group = queue.pop(0)
            if len(group[0]) < 1:
                continue
            rc = group[0][0]
            idx = self.getIdx(rc)
            if not nodes[idx]:
                nodes[idx] = Node(rc, True)
            current = nodes[idx]
            newGroup = list()
            visited = set()

            for word in group:
                character = word[0]
                if current.val != character:
                    if current.val in visited:
                        return ""
                    visited.add(current.val)

                    if not nodes[self.getIdx(character)]:
                        nodes[self.getIdx(character)] = Node(character)
                    childNode = nodes[self.getIdx(character)]
                    childNode.isRoot = False
                    current.childs.add(childNode)
                    current = childNode
                    if newGroup:
                        queue.append(newGroup)

                    newGroup = list()
                    if newGroup and not word[1:]:
                        return ""
                    if word[1:]:
                        newGroup.append(word[1:])
                else:
                    if newGroup and not word[1:]:
                        return ""
                    if word[1:]:
                        newGroup.append(word[1:])

            if newGroup:
                if current.val in visited:
                    return ""
                queue.append(newGroup)

        answer = ""
        roots = [node for node in nodes if node and node.isRoot]
        for node in nodes:
            print(node)
        visited = set()
        while roots:
            roots.sort(key=lambda x: x.val)
            target = roots.pop(0)
            if target.val in visited:
                return ""
            visited.add(target.val)
            answer += target.val

            for child in target.childs:
                roots.append(child)
        return answer
