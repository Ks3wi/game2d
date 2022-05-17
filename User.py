import Player
class User(Player.Player):
    def __init__(self, character, name):
        super().__init__(character)
        self.__name = name
    def GetName(self):
        return self.__name
    def Move(self):
        user_input = input("Move: ")
        if user_input == "a":
            if self._pos_x == 0:
                self._pos_x = 3
            else:
                self._pos_x -= 1
            #idz w lewo
        elif user_input == "d":
            if self._pos_x == 3:
                self._pos_x = 0
            else:
                self._pos_x += 1
            #idz w prawo
        elif user_input == "w":
            if self._pos_y == 0:
                self._pos_y = 3
            else:
                self._pos_y -= 1
            #idz w gore
        elif user_input == "s":
            if self._pos_y == 3:
                self._pos_y = 0
            else:
                self._pos_y += 1
            #idz w dol
        else:
            print("Wrong input")