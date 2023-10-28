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
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if (len(stack) == 0):
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


print(Solution().inorderTraversal(TreeNode(0, TreeNode(1, None, TreeNode(3)), TreeNode(2, TreeNode(4)))))
#print(Solution().inorderTraversal(TreeNode(1)))