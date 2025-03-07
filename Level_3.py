import time
import heapq

class TimeBasedCache:
    def __init__(self):
        self.cache = {}  # Stores key -> (value, expiryTime)
        self.expiry_heap = []  # Min-heap to track expirations (expiryTime, key)
    
    def _clean_expired_keys(self):
        """Removes expired keys from the cache."""
        current_time = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] <= current_time:
            expiry, key = heapq.heappop(self.expiry_heap)
            if key in self.cache and self.cache[key][1] <= current_time:
                del self.cache[key]
    
    def set(self, key, value, expiryTime):
        """Sets a key-value pair with an expiry timestamp."""
        self._clean_expired_keys()  # Remove expired keys before setting
        expiry_timestamp = time.time() + expiryTime
        self.cache[key] = (value, expiry_timestamp)
        heapq.heappush(self.expiry_heap, (expiry_timestamp, key))
    
    def get(self, key):
        """Retrieves the value if it exists and is not expired."""
        self._clean_expired_keys()  # Remove expired keys before fetching
        if key in self.cache:
            value, expiry = self.cache[key]
            if expiry > time.time():
                return value
            else:
                del self.cache[key]  # Remove expired key
        return None

# Example Usage
cache = TimeBasedCache()
cache.set("a", 100, 5)  # Key "a" with value 100, expires in 5 sec
cache.set("b", 200, 2)  # Key "b" with value 200, expires in 2 sec

print(cache.get("a"))  # Output: 100 (if within 5 sec)
time.sleep(3)
print(cache.get("b"))  # Output: None (expired)
print(cache.get("a"))  # Output: 100 (if within 5 sec)
time.sleep(3)
print(cache.get("a"))  # Output: None (expired)
