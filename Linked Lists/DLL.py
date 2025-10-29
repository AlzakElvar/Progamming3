class Node():
    def __init__(self, n_data, f_point = None, b_point = None):
        self.data = n_data
        self.point = f_point
        self.back = b_point

class d_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_forward(self):
        self.forward = True
        for val in  iter(self):
            print(val.data)

    def print_backward(self):
        self.forward = False
        print(self.tail.data)
        for val in  iter(self):
            print(val.data)
    
    def append_item(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = Node(item)
            self.head.point = self.tail
        else:
            temp = Node(item)
            p_back = self.tail
            self.tail.point = temp
            self.tail = temp
            self.tail.back = p_back

    def __iter__(self):
        if self.forward:
            self.pos = self.head
            return self

        else:
            self.pos = self.tail
            return self

    def __next__(self):
        if self.forward:
            
            if self.pos.point == None:
                raise StopIteration
            
            self.pos = self.pos.point   #Shifts pos on down the array
            return self.pos
        else:            
            
            if self.pos.back == None:
                raise StopIteration
            
            self.pos = self.pos.back
            return self.pos



brick = d_linked_list()


for i in range(15):
    brick.append_item(i)


print("Backward:")
brick.print_backward()


print("\nForward:")
brick.print_forward()
