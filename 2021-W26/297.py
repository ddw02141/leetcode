# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        nodes = [root]
        output = list()
        while any(nodes):
            for node in nodes:
                if node:
                    output.append(node.val)
                else:
                    output.append(None)
            nodes = [child for node in nodes for child in (node.left if node else None, node.right if node else None)]
        return str(output)

    def buildTree(self, values, index):
        node = TreeNode(values[index])
        if values[index] == None:
            return None
        if index * 2 + 1 < len(values):
            node.left = self.buildTree(values, index * 2 + 1)
        if index * 2 + 2 < len(values):
            node.right = self.buildTree(values, index * 2 + 2)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.replace("[", "").replace("]", "")
        l = [int(d) if d != "None" else None for d in data.split(", ")]
        if not any(l):
            None
        return self.buildTree(l, 0)


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
if __name__ == "__main__":
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))