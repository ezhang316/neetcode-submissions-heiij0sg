# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def findDiameterSubTree(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            heightL = findDiameterSubTree(root.left) + 1
            heightR = findDiameterSubTree(root.right) + 1

            self.res = max(self.res, (heightL + heightR - 2))

            return max(heightL, heightR)
        
        findDiameterSubTree(root)
        return self.res
