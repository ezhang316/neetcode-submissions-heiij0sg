# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def postorder(root):
            if not root:
                return True, None

            left = postorder(root.left)
            right = postorder(root.right)

            if not left[0] or not right[0]:
                return False, None
            
            if (left[1] and not left[1] < root.val) or (right[1] and not right[1] > root.val):
                return False, None
            
            return True, root.val
        
        return postorder(root)[0]