# Search Functions
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
        midpoint = (first+last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if a_list[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found


# Sort Functions
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
    sublistcount = len(a_list) // 2
    
    while sublistcount:
        for startpos in range(sublistcount):
            gap_insertion_sort(a_list, startpos, sublistcount)
        
        print('After increment of size', sublistcount, 'The list is', a_list)
        sublistcount //= 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        current = a_list[i]
        pos = i
        
        while pos >= gap and a_list[pos-gap] > current:
            a_list[pos] = a_list[pos-gap]
            pos -= gap
        
        a_list[pos] = current