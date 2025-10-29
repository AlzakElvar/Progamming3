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
        for val in  iter(self):
            print(val.data)
    
    def add_to_head(self, item):
        temp = Node(item, self.head)
        self.head.back = temp
        self.head = temp
    
    def append_item(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
            self.head.point = self.tail
        
        else:
            temp = Node(item, None, self.tail)
            self.tail.point = temp
            self.tail = temp

    def __iter__(self):
        if self.forward:
            self.next = self.head
            return self

        else:
            self.next = self.tail
            return self

    def __next__(self):
        if self.forward:
            
            self.pos = self.next

            if self.pos is None:
                raise StopIteration
            
            self.next = self.pos.point   #Shifts pos on down the array
            return self.pos
        else:            
            
            self.pos = self.next
            
            if self.pos is None:
                raise StopIteration
            
            self.next = self.pos.back
            return self.pos


brick = d_linked_list()

for i in range(5):
    brick.append_item(i)


brick.add_to_head("NEW HEAD")

print("Backward:")
brick.print_backward()

print("\nForward")
brick.print_forward()
