# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        output = []
        
        while queue:
            current, height = queue.popleft()
            if current.left:
                queue.append((current.left, height + 1))
            if current.right:
                queue.append((current.right, height + 1))
            
            if len(output) == height:
                output.append([current.val])
            else:
                output[height].append(current.val)
        
        return output

        
