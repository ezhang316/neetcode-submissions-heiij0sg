class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        heapq.heapify(self.heap)

        for n in nums[k:]:
            if self.heap[0] < n:
                heapq.heapreplace(self.heap, n)

    def add(self, val: int) -> int:
        # if not self.heap[0]:
        #     heapq.heappush(self.heap, val)
        #     return val

        if self.heap[0] < val:
            heapq.heapreplace(self.heap, val)
            return self.heap[0]
