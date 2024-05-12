class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[self.size()-1]


class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()


class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)