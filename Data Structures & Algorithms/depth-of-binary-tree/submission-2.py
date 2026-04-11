# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        maximum = 0

        while stack:
            current_node, current_depth = stack.pop()

            if not current_node:
                continue

            if current_depth > maximum:
                maximum = current_depth
            
            stack.append((current_node.right, current_depth + 1))
            stack.append((current_node.left, current_depth + 1))
        
        return maximum
            



            