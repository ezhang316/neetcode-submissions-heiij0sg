# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        right_nodes = []
        output = []

        while q:
            level_q = deque(q)
            q.clear()
            last_value = 101
            while level_q:
                current = level_q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                
                last_value = current.val
            output.append(last_value)

        return output


