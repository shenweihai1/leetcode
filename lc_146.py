# FIXME
class doublyLinked(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val 
        self.prev = prev
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.hash = {}
        self.head = None
        self.tail = None

    def get(self, key):
        pass


    def put(self, key, val):
        pass