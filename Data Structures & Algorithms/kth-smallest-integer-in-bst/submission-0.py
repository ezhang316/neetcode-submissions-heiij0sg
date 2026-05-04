# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res= None
        
        def inorder(root, n):
            if not root:
                return 0
            
            total = inorder(root.left, n) + 1 + n
            print(root.val, n, total)

            if total == k:
                nonlocal res
                res = root.val

            grand_total = inorder(root.right, total)
            if grand_total:
                return grand_total
            else:
                return total
            
        
        inorder(root, 0)

        return res
