import Board
import User
import Goal
import os

class Game:
    def __init__(self, p_chr, p_name, g_chr):
        self.__UserObject = User.User(p_chr, p_name)
        self.__GoalObject = Goal.Goal(g_chr)
        self.__BoardObject = Board.Board()
    def Play(self):
        while self.__UserObject.GetPoints() < 5:
            os.system("cls")
            print(self.__UserObject.GetPoints())
            self.__UserObject.SetPosition(2, 1)
            self.__GoalObject.SetPosition(0, 2)
            self.__BoardObject.SetPosition(self.__UserObject.Character(), self.__UserObject.GetPosX(), self.__UserObject.GetPosY())
            self.__BoardObject.SetPosition(self.__GoalObject.Character(), self.__GoalObject.GetPosX(), self.__GoalObject.GetPosY())
            self.__BoardObject.Display()
            input()
            self.__UserObject.AddPoints()