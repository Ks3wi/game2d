class Board:
    def __init__(self):
        self.__board = [
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ',' ',' ',' ']]
    def Display(self):
        for x in self.__board:
            for y in x:
                print("[", end="")
                print(y, end="")
                print("]", end="")
            print()
    def Reset(self):
        for x in self.__board:
            for y in x:
                print("[", end="")
                print(" ", end="")
                print("]", end="")
            print()
    def SetPosition(self, char, x, y):
        pass