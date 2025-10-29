class Node():
    def __init__(self, n_data, n_point = None):
        self.data = n_data
        self.point = n_point

class s_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def iterate_item(self):
        return iter(self)
        pass
    
    def append_item(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = Node(item)
            self.head.point = self.tail
        else:
            temp = Node(item)
            self.tail.point = temp
            self.tail = temp

    def __iter__(self):
        self.pos = self.head
        return self

    def __next__(self):
        if self.pos.point == None:
            raise StopIteration
        
        self.pos = self.pos.point   #Shifts pos on down the array
        return self.pos



brick = s_linked_list()


for i in range(5):
    brick.append_item(i)

itbrick = brick.iterate_item()
for val in itbrick:
    print(val.data)


