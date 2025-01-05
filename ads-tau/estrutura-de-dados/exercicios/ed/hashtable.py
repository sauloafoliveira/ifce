from typing import Generic, TypeVar, Self
from arraylist import ArrayList

K = TypeVar('K')
V = TypeVar('V')


class Hashtable(Generic[K, V]):

    def __init__(self):
        super().__init__()
        self._entries = []
       

    def clear(self):        
        self._entries = []
        

    def contains_key(self, key: K):
        for k, _ in self._entries:
            if k == key:
                return True
            
        return False
    

    def equals(self, other: Self) -> bool:
        for k, v in self._entries:
            if not other.contains_key(k) or other.get(k) == v:
                return False
            
        return True
    

    def first_key(self) -> K:
        for k, _ in self._entries:
            return k


    def get(self, key: K) -> V:
        for k, v in self._entries:
            if k == key:
                return v
            
        
    def is_empty(self) -> int:
        return self.size() == 0
    

    def keys(self) -> list[K]:
        return list(k for k, _ in self._entries)
    

    def last_key(self) -> K:
        last_entry = self._entries[-1]
        return last_entry[-1]
    

    def map(self, fn: callable) -> None:
        for i, (key, value) in enumerate(self._entries):
            result = fn(key, value)
            self._entries[i] = result


    def put(self, key: K, value: V):
        for i, (k, _) in enumerate(self._entries):
            if key == k:
                self._entries[i] = value
                return

        self._entries.append((key, value))
        

    def remove(self, key: K):
        for i, (k, _) in enumerate(self._entries):
            if key == k:
                del self._entries[i]   


    def size(self) -> int:
        return len(self._entries)
    

    def to_str(self) -> str:
        return ""
    

    def values(self) -> list[V]:
        return list(v for _, v in self._entries)

