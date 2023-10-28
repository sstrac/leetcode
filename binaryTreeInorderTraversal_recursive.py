class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if root is None:
            return res

        node = root

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            res.append(node.val)
            if node.right is not None:
                traverse(node.right)
                return
            return

        traverse(node)
        return res

#print(Solution().inorderTraversal(TreeNode(0, TreeNode(1, None, TreeNode(3)), TreeNode(2, TreeNode(4)))))
print(Solution().inorderTraversal(TreeNode(1)))