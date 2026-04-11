# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        visited_nodes = {None: (0, 0)}

        while stack:
            current_node = stack[-1]
            left = current_node.left
            right = current_node.right
            if left and left not in visited_nodes:
                stack.append(left)
            elif right and right not in visited_nodes:
                stack.append(right)
            else:
                current_node = stack.pop()
                left = current_node.left
                right = current_node.right

                left_height, left_diameter = visited_nodes[left]
                right_height, right_diameter = visited_nodes[right]
                visited_nodes[current_node] = (
                    1 + max(left_height, right_height)
                    , max(left_height + right_height, left_diameter, right_diameter)
                )

        return visited_nodes[root][1]
