import operator

class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj
    
    def get_root_val(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    
    if tree:
        res1 = postordereval(tree.get_left_child())
        res2 = postordereval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()


def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def printexp(tree):
    string_val = ""
    
    if tree:
        string_val = '(' + printexp(tree.get_left_child())
        string_val = string_val + str(tree.get_root_val())
        string_val = string_val + printexp(tree.get_right_child())+')'
    
    return string_val


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
    
    def min_child(self,i):
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
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val('hello')
    print(r.get_right_child().get_root_val(), end='\n\n')
    
    bh = BinaryHeap()
    bh.build_heap([9, 5, 6, 2, 3])
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())