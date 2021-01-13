from field import Field


class Sudoku:

    def __init__(self):
        self.__field = Field()
        self.__finished = False

    def __valid_position(self, i, j, value):
        for y in range((i // 3) * 3, (i // 3) * 3 + 3):
            for x in range((j // 3) * 3, (j // 3) * 3 + 3):
                if self.__field.grid[y][x] == value:
                    return False
        for t in range(9):
            if (self.__field.grid[i][t] == value or
                    self.__field.grid[t][j] == value):
                return False
        return True

    def finished(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if self.__field.grid[i][j] == '*':
                    count += 1
        return count == 0

    # clever algorithms for suckers!
    # simple, understandable, reliable solution is there
    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.__field.grid[i][j] == '*':
                    for value in range(1, 10):
                        if self.__valid_position(i, j, value):
                            self.__field.grid[i][j] = value
                            self.solve()
                            if not self.__finished:
                                self.__field.grid[i][j] = '*'
                    return
        self.__finished = True

    def turn(self, i, j, value):
        if (0 <= i <= 8 and
                0 <= j <= 8 and
                1 <= value <= 9):
            if self.__valid_position(i, j, value):
                self.__field.grid[i][j] = value
                return True
            else:
                return False
        else:
            return False

    def print_field(self):
        self.__field.print_field()

    def gen_field(self, n):
        self.__field.gen_field(n)

    def set_field(self, field):
        self.__field.grid = field