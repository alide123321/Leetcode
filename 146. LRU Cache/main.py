class LRUCache:

    def __init__(self, capacity: int):
        self.CAP = capacity
        self.cache = {}
        self.dq = deque()
        

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.dq.remove(key)
            self.dq.append(key)
            return self.cache[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dq.remove(key)
            self.dq.append(key)
            self.cache[key] = value
            return

        if len(self.dq) >= self.CAP:
            removeKey = self.dq.popleft()
            self.cache.pop(removeKey, None)
        
        self.cache[key] = value
        self.dq.append(key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)