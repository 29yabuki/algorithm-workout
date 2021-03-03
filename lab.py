def sequential(a_list, item):
    pos = 0
    found = False
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    
    return found


def ordered_sequential(a_list, item):
    pos = 0
    found = False
    stop = False
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    
    return found


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first+last)//2
        if a_list[midpoint] == item:
            found = True
        else:
            if a_list[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    return found


def bubble_sort(a_list):
    for pairs in range(len(a_list)-1, 0, -1):
        for i in range(pairs):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp

                                                                                                                                                                                                                                                                                                                                                                                                                          
def short_bubble_sort(a_list):
    pairs = len(a_list) - 1
    exchange = True
    
    while pairs > 0 and exchange:
        exchange = False
        for i in range(pairs):
            if a_list[i] > a_list[i+1]:
                exchange = True
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
        
        pairs -= 1


def selection_sort(a_list):
    for i in range(len(a_list)):
        current_min = i
        
        for j in range(i+1, len(a_list)):
            if a_list[j] < a_list[current_min]:
                current_min = j

        if current_min != i:
            temp = a_list[i]
            a_list[i] = a_list[current_min]
            a_list[current_min] = temp

                                                                                                                                         
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        current = a_list[i]
        pos = i
        
        while pos > 0 and a_list[pos-1] > current:
            a_list[pos] = a_list[pos-1]
            pos -= 1

        a_list[pos] = current


def shell_sort(a_list):
    sublistcount = len(a_list)//2
    
    while sublistcount:
        
        for startpos in range(sublistcount):
            gapInsertionSort(a_list, startpos, sublistcount)
        
        print('After increment of size', sublistcount, 'The list is', a_list)
        sublistcount//=2


def gapInsertionSort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        current = a_list[i]
        pos = i
        
        while pos >= gap and a_list[pos-gap] > current:
            a_list[pos] = a_list[pos-gap]
            pos -= gap
        
        a_list[pos] = current


class Node():
    
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

                   
class LinkedList():
    
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
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
                return count
            else:
                count += 1
                current = current.get_next()
        
        return -1

    # index type II          
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

    # pop(self): removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.                                           
    def pop(self):
        current = self.head
        previous = None
        
        if current.get_next() == None:
            self.head = None
        else:
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
        
        return current.get_data()

    # poppos(self, pos): removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.              
    def pospop(self, pos):
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

mylist = LinkedList()
mylist.add(3)
mylist.add(4)
mylist.add(1)
print(mylist.index(3))
print(mylist.remove(3))
print(mylist.size())
print(mylist.pop())
print(mylist.size())