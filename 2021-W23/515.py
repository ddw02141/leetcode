# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        answerMap = dict()
        answerList = list()
        row = [root]
        while any(row):
            answerList.append(max(node.val for node in row))
            row = [child for node in row for child in (node.left, node.right) if child]
        return answerList