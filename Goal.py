from random import random
import Player
class Goal(Player.Player):
    def __init__(self, character):
        super().__init__(character)
    def Move(self):
        self._pos_x = random(0, 3)
        self._pos_y = random(0, 3)