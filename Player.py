class Player:
    def __init__(self, character):
        self._pos_x = 0
        self._pos_y = 0
        self.character = character
    def GetPosX(self):
        return self._pos_x
    def GetPosy(self):
        return self._pos_y
    def Character(self):
        return self._character
