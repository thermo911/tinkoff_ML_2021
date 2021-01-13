import pickle
from sudoku import Sudoku


class Game:
    def __init__(self):
        self.__sudoku = Sudoku()
        self.__initialized = False

    def __save_game(self):
        if self.__initialized:
            pickle_out = open("lastgame.pickle", "wb")
            pickle.dump(self.__sudoku, pickle_out)
            pickle_out.close()
            print("game saved")
            return True
        else:
            print("field is empty")
            return False

    def __load(self):
        try:
            pickle_in = open("lastgame.pickle", "rb")
            self.__sudoku = pickle.load(pickle_in)
            self.__initialized = True
            return True
        except FileNotFoundError:
            print("saved game not found")
            return False

    def __human_session(self):
        while not self.__sudoku.finished():
            try:
                commands = [s for s in input("turn: ").split()]
                if commands[0] == "save":
                    if self.__save_game():
                        break
                tokens = [int(x) for x in commands]
                if len(tokens) != 3:
                    continue
                if not self.__sudoku.turn(tokens[0] - 1, tokens[1] - 1, tokens[2]):
                    print("incorrect turn")
                    continue
                else:
                    self.__sudoku.print_field()
                    if self.__sudoku.finished():
                        print("You win!")
                        break
            except BaseException:
                print("incorrect input")

    def __pc_session(self):
        print("Hmm... I'm thinking...")
        self.__sudoku.solve()
        print("That's all I've solved")
        self.__sudoku.print_field()

    def start(self):
        mode = ""
        while mode != '1' and mode != '2':
            mode = input("Who will play? (1 - human, 2 - pc) :")
        mode = int(mode)
        if mode == 1:
            loading = input("Enter 'load' to load last saved game: ")
            if loading == "load" and self.__load():
                print("successfully loaded")
                self.__sudoku.print_field()
                self.__human_session()
            else:
                filled_cells = int(input("Generating the field... Cells to be filled: "))
                self.__sudoku.gen_field(filled_cells)
                self.__sudoku.print_field()
                self.__initialized = True
                self.__human_session()
        elif mode == 2:
            print("You have challenged Artificial Intelligence!")
            print("Enter field, noob!")
            print("Be respectful to Master! Make sure that your sudoku has the solution!")
            self.__read_field()
            self.__sudoku.print_field()
            self.__pc_session()


    def __read_field(self):
        field = []
        while len(field) < 9:
            try:
                row = [x for x in input("row {0}: ".format(len(field)+1)).split()]
                if len(row) != 9:
                    print("incorrect input")
                    continue
                correct = True
                for i in range(9):
                    if row[i] != '*':
                        if not 1 <= int(row[i]) <= 9:
                            correct = False
                            break
                if correct:
                    field.append(row)
                else:
                    print("incorrect input")
            except ValueError:
                print("incorrect input")
        self.__sudoku.set_field(field)


