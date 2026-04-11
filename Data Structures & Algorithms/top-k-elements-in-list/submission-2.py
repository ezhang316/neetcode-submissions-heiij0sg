class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(int)
        for n in nums:
            dictionary[n] += 1
        
        print(dictionary)
        min_heap = []
        for i in range(k):
            if dictionary:
                key, value = dictionary.popitem()
                min_heap.append((value, key))

        for key, value in dictionary.items():
            if value > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (value, key))

        result = []
        for item in min_heap:
            result.append(item[1])

        return result