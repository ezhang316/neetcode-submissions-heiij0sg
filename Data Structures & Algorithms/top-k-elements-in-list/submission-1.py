class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for n in nums:
            dictionary[n] += 1
        

        min_heap = []
        for i in range(k):
            if dictionary:
                min_heap.append(dictionary.popitem())

        for key, value in dictionary.items():
            if value > min_heap[0][1]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (key, value))

        result = []
        for item in min_heap:
            result.append(item[0])

        return result