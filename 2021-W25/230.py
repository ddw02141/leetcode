# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # in-order traversal
        l = list()

        def trip(node):
            if not node:
                return
            trip(node.left)
            l.append(node.val)
            trip(node.right)

        trip(root)
        return l[k - 1]
