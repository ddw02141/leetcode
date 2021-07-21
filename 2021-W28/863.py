# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
# Dist(n1, n2) = Dist(lca, n1) + Dist(lca, n2)
# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        answer = list()
        nodes = [root]
        while any(nodes):
            for node in nodes:
                # print("node",node.val,"distance",self.findDistance(root, node, target))
                if self.findDistance(root, node, target) == k:
                    answer.append(node.val)
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return answer

    def findDistance(self, root, node, target):
        lca = self.findLca(root, node, target)
        return self.findLevel(lca, node) + self.findLevel(lca, target)

    def findLca(self, root, node, target):
        if not root:
            return None

        if root.val == node.val or root.val == target.val:
            return root

        leftLca = self.findLca(root.left, node, target)
        rightLca = self.findLca(root.right, node, target)

        if leftLca and rightLca:
            return root
        elif leftLca:
            return leftLca
        else:
            return rightLca

    def findLevel(self, root, target):
        nodes = [root]
        nodeLevel = 0
        while any(nodes):
            for node in nodes:
                if node == target:
                    return nodeLevel
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
            nodeLevel += 1
