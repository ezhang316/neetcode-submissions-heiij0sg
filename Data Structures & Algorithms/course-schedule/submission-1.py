class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = []
        
        graph = defaultdict(list)

        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        def dfs(node):
            if node in seen:
                return False
            
            if graph[node] == []:
                return True

            seen.append(node)

            for edge in graph[node]:
                if not dfs(edge):
                    return False
            
            seen.pop()

            graph[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True