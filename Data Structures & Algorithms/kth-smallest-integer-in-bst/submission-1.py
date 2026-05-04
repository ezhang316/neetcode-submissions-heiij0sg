# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = None
        count = 0
        
        def inorder(root):
            if not root:
                return
            nonlocal count
            
            inorder(root.left)
            
            count += 1

            if count == k:
                nonlocal res
                res = root.val

            grand_total = inorder(root.right)
            
        
        inorder(root)

        return res
