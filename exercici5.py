#tauler d'escacs
class Piece:
   def __init__(self, type:str, isWhite:bool, positionY:int, positionX:int):
        self.type = type
        self.isWhite = True
        self.positionY = positionY
        self.positionX = positionX


def setUpBoard():
     print("Benvingut al tauller d'escacs")
     board = [
          ['□','■','□','■','□','■','□','■','1'],
          ['■','□','■','□','■','□','■','□','2'],
          ['□','■','□','■','□','■','□','■','3'],
          ['■','□','■','□','■','□','■','□','4'],
          ['□','■','□','■','□','■','□','■','5'],
          ['■','□','■','□','■','□','■','□','6'],
          ['□','■','□','■','□','■','□','■','7'],
          ['■','□','■','□','■','□','■','□','8'],
          ['A','B','C','D','E','F','G','H',' ']
     ]
    
     for row in board:
        print(" ".join(row))

     pieces = [
         Piece("♖", True, 0, 0),
         Piece("♘", True, 0, 1),
         Piece("♗", True, 0, 2),
         Piece("♕", True, 0, 3),
         Piece("♔", True, 0, 4),
         Piece("♗", True, 0, 5),
         Piece("♘", True, 0, 6),
         Piece("♖", True, 0, 0)
     ]
     
     player1Movement = input(Piece)
     

     move = board[player1Movement]

   
setUpBoard()
