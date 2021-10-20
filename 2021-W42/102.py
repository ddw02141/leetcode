# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = list()
        nodes = [root]
        while any(nodes):
            ans = [node.val for node in nodes if node]
            answer.append(ans)
            nodes = [child for node in nodes if node for child in (node.left, node.right)]

        return answer
