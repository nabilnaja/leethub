class TimeMap:
    """
    Time complexity: get -> O(log n), set -> O(1)  
    """
    def __init__(self):
        self.dt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        return self.search(self.dt[key], timestamp)
        
    def search(self, values, timestamp):
        l, r = 0, len(values) - 1
        if not self:
            return None
        res = ''
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] < timestamp:
                res = values[l][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)