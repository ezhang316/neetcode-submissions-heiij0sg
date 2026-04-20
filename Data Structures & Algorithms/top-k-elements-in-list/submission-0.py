class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for n in nums:
            dictionary[n] += 1
        

        min_heap = []
        for i in range(k):
            if dictionary:
                min_heap.append(dictionary.popitem()[0])

        for key, value in dictionary.items():
            if value > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, key)

        return min_heap