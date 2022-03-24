from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        dfs를 통해 root ~ child value의 배열을 만듦
        만들때는 시간 복잡도 감소를 위해 prefix sum을 사용
        leaf node를 만났다면, index 두 개를 잡고 두 개의 차가 targetSum이라면 answer +1
        """
        if not root:
            return 0

        def dfs(node, prefixSum):
            prefixSum.append(prefixSum[-1] + node.val)
            # print("node", node.val, "prefixSum", prefixSum)
            for i in range(len(prefixSum) - 1):
                if prefixSum[-1] - prefixSum[i] == targetSum:
                    self.answer += 1

            if not node.left and not node.right:
                del prefixSum[-1]
                return

            if node.left:
                dfs(node.left, prefixSum)
            if node.right:
                dfs(node.right, prefixSum)

            del prefixSum[-1]

        dfs(root, [0])

        return self.answer
