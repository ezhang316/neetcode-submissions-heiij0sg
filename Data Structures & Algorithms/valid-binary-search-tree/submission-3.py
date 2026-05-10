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
                return True, None, None

            left = postorder(root.left)
            right = postorder(root.right)

            if not left[0] or not right[0]:
                return False, None, None
            
            if (left[2] is not None and not left[2] < root.val) or (right[1] is not None and not right[1] > root.val):
                return False, None, None

            min = left[1]
            max = right[2]
            
            if min is None:
                min = root.val
            if max is None:
                max = root.val

            return True, min, max
        
        return postorder(root)[0]