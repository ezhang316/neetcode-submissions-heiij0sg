class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        edge_graph = {i: [] for i in range(n)}
        for i, j in edges:
            edge_graph[i].append(j)
            edge_graph[j].append(i)


        def dfs(v, vp):
            if v in visited:
                return False
            
            visited.add(v)

            for v2 in edge_graph[v]:
                if v2 == vp:
                    continue
                if not dfs(v2, v):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
                