# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        current_val = preorder[0]

        left_branch_inorder = inorder[:inorder.index(current_val)]
        left_branch_preorder = preorder[1:inorder.index(current_val) + 1]
        left_node = self.buildTree(left_branch_preorder, left_branch_inorder)
        
        right_branch_inorder = inorder[inorder.index(current_val) + 1:]
        right_branch_preorder = preorder[inorder.index(current_val) + 1:]
        right_node = self.buildTree(right_branch_preorder, right_branch_inorder)

        current = TreeNode(current_val, left_node, right_node)

        return current