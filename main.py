import Board
import Goal
import User
import game

B1 = Board.Board()
B1.Display()
B1.SetPosition('x', 0, 1)
B1.Display()
B1.Reset()
B1.SetPosition('o', 0, 2)
B1.Display()

U1 = User.User('X', 'player1')

U1.AddPoints()
print(U1.GetPoints())

G1 = Goal.Goal('o')
print("position check")
print(G1.GetPosX())
print(G1.GetPosY())
G1.Move()
print(G1.GetPosX())
print(G1.GetPosY())

Game1 = game.Game('X', 'player1', 'o')
Game1.Play()



