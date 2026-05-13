# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf
        def dfs(root):
            if not root:
                return None
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            nonlocal res
            if left_max is None and right_max is None:
                return root.val
            elif right_max is None:
                current_max = left_max + root.val
                res = max(res, current_max)
                return max(
                    current_max,
                    root.val
                )

            elif left_max is None:
                current_max = right_max + root.val
                res = max(res, current_max)
                return max(
                    current_max,
                    root.val
                )
            else:
                current_max = max(
                    left_max + root.val + right_max,
                    left_max + root.val,
                    right_max + root.val
                )
                res = max(res, current_max)
                return max(
                    left_max + root.val,
                    right_max + root.val
                )
        
        dfs(root)
        if res == -math.inf:
            return 0
        return res