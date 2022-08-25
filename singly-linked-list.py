# Node Class
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, item):
        self.data = item
    
    def get_next(self):
        return self.next
    
    def set_next(self, item):
        self.next = item


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def append(self, item):
        current = self.head
        
        if current:
            while current.get_next() != None:
                current = current.get_next()
            
            current.set_next(Node(item))
        else:
            self.head = Node(item)
    
    def insert(self, pos, item):
        count = 0
        temp = Node(item)
        previous = None
        current = self.head
        
        if pos == 0:
            self.add(item)
        else:
            while count < pos:
                count += 1
                previous = current
                current = current.get_next()
            temp.set_next(current)
            previous.set_next(temp)
    
    def size(self):
        count = 0
        current = self.head
        
        while current != None:
            count += 1
            current = current.get_next()
        
        return count
    
    def search(self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def index(self, item):
        count = 0
        current = self.head
        
        while current != None:
            if current.get_data() == item:
                return count
            else:
                count += 1
                current = current.get_next()
        
        return -1
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            pass
    
    def pop(self, pos=-1):
        count = 0
        current = self.head
        previous = None
        
        if pos == 0:
            self.head = current.get_next()
        elif pos == -1:
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
        else:
            while count < pos:
                count += 1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
        
        return current.get_data()
    
    def __repr__(self):
        a_list = []
        current = self.head
        
        while current != None:
            a_list.append(current.get_data())
            current = current.get_next()
        
        list_str = ', '.join(str(i) for i in a_list)
        return f'[{list_str}]'


# Pythonic Node Class
class PythonicNode:
    def __init__(self, item):
        self._data = item
        self._next = None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, item):
        self._data = item
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, item):
        self._next = item


# main event loop
mylist = LinkedList()
mylist.add(3)
mylist.add(4)
mylist.add(1)
print(mylist)
print("index of 3 in linked list:", mylist.index(3))
mylist.remove(3)
print(mylist)
print("current size of linked list:", mylist.size())
print("last value popped:", mylist.pop())
print("current size of linked list:", mylist.size())
print(mylist)