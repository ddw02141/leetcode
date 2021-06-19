# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        nodes = [root]
        maxi = float("-inf")
        maxiLevel = -1
        level = 1
        while any(nodes):
            sumi = sum(node.val for node in nodes)
            if maxi < sumi:
                maxi = sumi
                maxLevel = level
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
            level += 1
        return maxLevel