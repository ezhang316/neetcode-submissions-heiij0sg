# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def rec(node, largest):
            if not node:
                return
            
            if node.val >= largest:
                nonlocal res
                res += 1
            
            next_largest = max(largest, node.val)

            rec(node.left, next_largest)
            rec(node.right, next_largest)
        
        rec(root, root.val)

        return res