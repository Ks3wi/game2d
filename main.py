import Board
B1 = Board.Board()
B1.Display()
B1.SetPosition('x', 0, 1)
B1.Display()
B1.Reset()
B1.SetPosition('o', 0, 2)
B1.Display()

U1 = User.User('X', 'player1')