import timeit


class LRUCache:
    def __init__(self, capacity: int):
        self.cache_map = {}
        self.capacity = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.cache_map.keys():
            value = self.cache_map.get(key)
            if key in self.lru:
                self.lru.remove(key)
                self.lru.insert(0, key)
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_map.keys():
            while len(self.cache_map) >= self.capacity:
                if self.lru:
                    self.cache_map.pop(self.lru.pop())
                    self.lru.insert(0, key)
        self.cache_map[key] = value
        return None


if __name__ == '__main__':
    lru = LRUCache(2)
    start = timeit.default_timer()
    methods = ["put", "put", "get", "put", "put", "get"]
    params = [[2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    print([getattr(lru, method)(*params[i]) for i, method in enumerate(methods)])
    end = timeit.default_timer()
    print(end - start)
