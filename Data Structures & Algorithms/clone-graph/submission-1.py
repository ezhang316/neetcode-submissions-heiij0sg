"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return
        
        seen = {}

        def dfs(current):

            val = current.val
            
            if val in seen.keys():
                return seen[val]

            seen[val] = Node(val)
            
            neighbors = []

            for n in current.neighbors:
                neighbors.append(dfs(n))

            seen[val].neighbors = neighbors

            return seen[val]

        return dfs(node)