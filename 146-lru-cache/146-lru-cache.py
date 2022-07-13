class DoubleLinkedList():
    
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.previous = None
        self.next = None
    
class LRUCache:
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev, next = node.prev, node.next        
        prev.next, next.prev = next, prev
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DoubleLinkedList(0,0)
        self.tail = DoubleLinkedList(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        else :
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
            return
        node = DoubleLinkedList(value, key)
        if self.size >= self.capacity:
            to_remove = self._pop_tail()
            self.cache.pop(to_remove.key)
            self.size -= 1
        self._add_node(node)
        self.cache[key] = node
        self.size += 1
            
        
        

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)