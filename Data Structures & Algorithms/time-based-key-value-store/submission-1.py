import bisect

class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_dict[key]
        i = bisect.bisect_right(arr, timestamp, key=lambda item: item[0])
        if i == 0:
            return ""
        return arr[i - 1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)