# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        curr_depth = 0
        stack = []
        while True:
            while root:
                curr_depth += 1
                stack.append(root)
                root = root.left

            if len(stack) == 0:
                return depth

            curr_depth = len(stack)
            root = stack.pop().right

            if curr_depth > depth:
                depth = curr_depth
