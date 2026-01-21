import random as r

game_running = True


class Grid:
    def __init__(self, grid = None):
        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for _ in range(3)] for _ in range(3)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def place(self, place, i):
        if i == 0:
            if self.grid[2 - ((place -1) // 3)][(place -1) % 3] == 0:
                self.grid[2 - ((place -1) // 3)][(place -1) % 3] = 1
                return True
            else:
                return False
        else:
            if self.grid[2 - ((place -1) // 3)][(place -1) % 3] == 0:
                self.grid[2 - ((place -1) // 3)][(place -1) % 3] = 2
                return True
            else:
                return False

    def get_space(self, i):
        return self.grid[2 - ((i-1) // 3)][(i -1) % 3]

    def is_space(self):
        for i in self.grid:
            for j in i:
                if j == 0:
                    return True
        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.turn = 0
        self.links = []

class Tree:
    def __init__(self, root:Grid):
        self.root = Node(root)
        self.eyes = Eyes(self.root)

    def grow(self):
        for a in range(9):
            if self.root.data.get_space(a) == 0:
                temp = self.root.data
                temp.place(a, (self.root.turn % 2))
                self.root.links.append(Node(temp))

    def loop(self):
        for i in self.root.links:
            if i.links:
                print(i.data)
                for j in i.links:
                    print(j.data)

class Eyes:
    def __init__(self, grid):
        self.grid = grid

    def check_row(self, i):
        row = 1 + (i * 3)

        for j in range(2):
            if self.grid.get_space(row) == 0:
                return False

            if self.grid.get_space(row) != self.grid.get_space(row + j + 1):
                return False
        return True

    def check_column(self, i):
        col = i + 1

        for j in range(2):
            if self.grid.get_space(col) == 0:
                return False

            if self.grid.get_space(col) != self.grid.get_space(col + ((j + 1) * 3)):
                return False
        return True

    def check_diagonal(self, i):
        if i == 0:
            start = 1
            mult = 4
        else:
            start = 3
            mult = 2

        for j in range(2):
            if self.grid.get_space(start) == 0:
                return False

            if self.grid.get_space(start) != self.grid.get_space(start + ((j + 1) * mult)):
                return False
        return True

    def winner(self):
        for a in range(3):
            if self.check_row(a):
                if self.grid.get_space(1 + (a * 3)) == 1:
                    return 0
                else:
                    return 1

            if self.check_column(a):
                if self.grid.get_space(a + 1) == 1:
                    return 0
                else:
                    return 1

        for a in range(2):
            if self.check_diagonal(a):
                if a == 0:
                    if self.grid.get_space(1) == 0:
                        return 0
                    else:
                        return 1
                else:
                    if self.grid.get_space(3) == 0:
                        return 0
                    else:
                        return 1
        return False


def traverse(root):
    if root:
        current = root
        for i in current.links:
            if i.data.winner() == 1:
                return -1
            elif i.data.winner() == 2:
                return 1
            else:
                return None

    return None

g = Grid()
e = Eyes(g)


if __name__ == '__main__':
    difficulty = int(input("Please choose a difficulty (0, 1) "))
    while game_running:

        ### PLAYER'S TURN START
        spot = int(input("Please select a space (1-9) to place an X  "))

        valid = g.place(spot, 0)

        while not valid:
            print("Invalid input")
            spot = int(input("Please select a space (1-9) to place an X  "))
            valid = g.place(spot, 0)
        ###PLAYER'S TURN END

        if not g.is_space():
            print("Board full")
            if e.winner() == 0:
                print("You win")
            elif e.winner() == 1:
                print("Bot wins")
            else:
                print("Draw")
            game_running = False

        if difficulty == 0:
            valid = g.place(r.randint(1, 9), 1)
            while not valid:
                valid = g.place(r.randint(1, 9), 1)
        else:
            pass
        #    g.min_max()


        g.print_grid()

        temp = e.winner()
        if temp is not False:
            if temp == 0:
                print("You win")
            elif temp == 1:
                print("Bot wins")
            game_running = False
