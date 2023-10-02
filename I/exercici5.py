#tauler d'escacs
def setUpBoard(size):
    abc = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M']
    board = []
    for yIndex in range(size):
        row = []
        for xIndex in range(size):
            row.insert(xIndex, getCell(xIndex, yIndex))
        row.append(yIndex+1)
        board.insert(yIndex,row)
    board.append(abc[:size]) #para el tamaño de la lista de letras
    return board    
    
def getCell(x, y): #obtener las fichas del tablero
    if((x + y) % 2 == 0): return '■'
    return '□'


def chess(size):
     print("Benvingut al tauller d'escacs")
     board2 = setUpBoard(size)
     for row in board2:
        print(row)
    
chess(8)
