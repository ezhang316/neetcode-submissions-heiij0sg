# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def findSubTreeHeight(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            
            l, r = findSubTreeHeight(root.left), findSubTreeHeight(root.right)
            
            if abs(l - r) > 1:
                res = False

            return max(l, r) + 1

        findSubTreeHeight(root)
        return res
        