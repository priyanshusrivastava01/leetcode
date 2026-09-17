# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: TreeNode | None) -> TreeNode | None:
#         if not root:
#             return

#         root.left, root.right = root.right, root.left

#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         return root

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if not root:
            return


        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
