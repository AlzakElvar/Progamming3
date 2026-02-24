class Node:
    def __init__(self, x):
        self.data = x
        self.links = []

class Tree:
    def __init__(self):
        self.root = Node(0)

    def grow(self):
        for i in range(9):
            self.root.links.append(Node(i))

            for j in range(9):
                self.root.links[i].links.append(Node((i, j)))

    def loop(self):
        for i in self.root.links:
            if i.links:
                print(i.data)
                for j in i.links:
                    print(j.data)

result = None
class Trav:
    def __init__(self):
        self.result = None

    def traverse(self, root):
        if root:
#            print(root.data)
            current = root
            for i in current.links:
                if i:
                    if i.data == (3,4):
                        self.result = i
                        return i
                    else:
                        self.traverse(i)

        return self.result

if __name__ == '__main__':
    tree = Tree()
    tree.grow()
    trav = Trav()
    print(trav.traverse(tree.root).data)
    #tree.loop()