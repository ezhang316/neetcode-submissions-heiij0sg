class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for _ in range(len(temperatures))]
        warmer_not_found = []

        for i in range(len(temperatures)):
            if warmer_not_found:
                while warmer_not_found and warmer_not_found[0][0] < temperatures[i]:
                    temp = heapq.heappop(warmer_not_found)
                    res[temp[1]] = i - temp[1]
            
            heapq.heappush(warmer_not_found, (temperatures[i], i))
        
        return res