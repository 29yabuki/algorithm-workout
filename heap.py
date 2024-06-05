class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0
    
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2
    
    def perc_down(self, i):
        while (i * 2) <= self.curr_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = temp
            i = mc
    
    def insert(self, k):
        self.heap_list.append(k)
        self.curr_size = self.curr_size + 1
        self.perc_up(self.curr_size)
    
    def min_child(self, i):
        if i * 2 + 1 > self.curr_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size = self.curr_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval
    
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.curr_size = len(a_list)
        self.heap_list = [0] +  a_list[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.build_heap([9, 5, 6, 2, 3])
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())