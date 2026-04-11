class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:self.k]
        heapq.heapify(self.heap)

        for n in nums[self.k:]:
            if self.heap[0] < n:
                heapq.heapreplace(self.heap, n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]