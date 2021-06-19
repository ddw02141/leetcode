# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answerMap = dict()
        answerList = list()
        def trip(cur, level):
            if not cur:
                return
            answerMap[level] = cur.val
            trip(cur.left, level + 1)
            trip(cur.right, level + 1)
        trip(root, 0)
        for num in range(100 + 1):
            if num not in answerMap:
                break
            answerList.append(answerMap[num])
        return answerList