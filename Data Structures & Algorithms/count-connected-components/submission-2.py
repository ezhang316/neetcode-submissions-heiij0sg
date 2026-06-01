class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d = {i: [] for i in range(n)}

        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])



        components = 0


        def dfs(e):
            if seen[e]:
                return True
            
            seen[e] = True
            
            for child_e in d[e]:
                dfs(child_e)

            return False



        seen = [False for _ in range(n)]
        for v in range(n):
            if not dfs(v):
                components += 1

        
        return components