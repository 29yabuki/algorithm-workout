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

    # isEmpty(): tests to see whether the list is empty. It needs no parameters and returns a boolean value.                                    
    def is_empty(self):
        return self.head == None

    # add(item): adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    # append(item): adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.             
    def append(self, item):
        current = self.head
        
        if current:
            while current.get_next() != None:
                current = current.get_next()
            
            current.set_next(Node(item))
        else:
            self.head = Node(item)

    # insert(pos,item): adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.      
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

    # size(): returns the number of items in the list. It needs no parameters and returns an integer.                             
    def size(self):
        count = 0
        current = self.head
        
        while current != None:
            count += 1
            current = current.get_next()
        
        return count

    # search(self, item): searches for the item in the list. It needs the item and returns a boolean value.                                                  
    def search(self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found

    # index(self, item): returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
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

    # remove(self, item): removes the item from the list.                                                                        
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

    # pop(self, pos=0): removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.                                            
    def pop(self, pos=0):
        count = 0
        current = self.head
        previous = None
        
        if pos == 0:
            self.head = current.get_next()
        else:
            while count < pos:
                count += 1
                previous = current
                current = current.get_next()
            previous.set_next(current.get_next())
        
        return current.get_data()

    # repr(self): prints a representation of the linked list in a list format
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