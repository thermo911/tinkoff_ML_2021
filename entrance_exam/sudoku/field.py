import random


class Field:
    def __init__(self):
        self.grid = None
        random.seed()

    def __transpose(self):
        self.grid = [[self.grid[i][j] for i in range(9)] for j in range(9)]

    def __swap_columns(self, column1=0, column2=0):
        if column1 == 0 and column2 == 0:
            zone = random.randint(0, 2)
            column1 = random.randint(zone * 3, zone * 3 + 2)
            column2 = column1
            while column2 == column1:
                column2 = random.randint(zone * 3, zone * 3 + 2)
        for i in range(9):
            self.grid[i][column1], self.grid[i][column2] = self.grid[i][column2], self.grid[i][column1]

    def __swap_rows(self, row1=0, row2=0):
        if (row1 == 0) and (row2 == 0):
            zone = random.randint(0, 2)
            row1 = random.randint(zone * 3, zone * 3 + 2)
            row2 = row1
            while row2 == row1:
                row2 = random.randint(zone * 3, zone * 3 + 2)
        self.grid[row1], self.grid[row2] = self.grid[row2], self.grid[row1]

    def __swap_horizontal_zones(self, zone1=0, zone2=0):
        if zone1 == 0 and zone2 == 0:
            zone1 = random.randint(0, 2)
            zone2 = zone1
            while zone2 == zone1:
                zone2 = random.randint(0, 2)
        for j in range(3):
            self.__swap_columns(zone1 * 3 + j, zone2 * 3 + j)

    def __swap_vertical_zones(self, zone1=0, zone2=0):
        if zone1 == 0 and zone2 == 0:
            zone1 = random.randint(0, 2)
            zone2 = zone1
            while zone2 == zone1:
                zone2 = random.randint(0, 2)
        for i in range(3):
            self.__swap_rows(zone1 * 3 + i, zone2 * 3 + i)

    def gen_field(self, n):
        self.grid = [[((i * 3 + i // 3 + j) % 9 + 1) for j in range(9)] for i in range(9)]
        for i in range(20):
            key = random.randint(0, 4)
            if key == 0:
                self.__transpose()
            elif key == 1:
                self.__swap_columns()
            elif key == 2:
                self.__swap_rows()
            elif key == 3:
                self.__swap_horizontal_zones()
            else:
                self.__swap_vertical_zones()
        if n < 18:
            n = 18
        i = 0
        while i < 81 - n:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if self.grid[y][x] != '*':
                self.grid[y][x] = '*'
                i += 1

    def print_field(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], "", end="")
                if j == 2 or j == 5:
                    print("| ", end="")
            if i == 2 or i == 5:
                print("\n---------------------")
            else:
                print()
