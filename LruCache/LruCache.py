class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.cache = {}

    def remove(self, node):
        behind_node = node.prev
        ahead_node = node.next

        behind_node.next = ahead_node
        ahead_node.prev = behind_node

        node.next = None
        node.prev = None


    def add_to_recent(self, node):
        prev_recent = self.head.next
        node.next = prev_recent
        prev_recent.prev = node
        
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.add_to_recent(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                removed_node = self.tail.prev
                del self.cache[removed_node.key]
                self.remove(removed_node)

            self.add_to_recent(node)
        else:
            node = self.cache[key]
            node.value = value
            self.cache[key] = node

            self.remove(node)
            self.add_to_recent(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
