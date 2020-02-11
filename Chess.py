import Piece
from pprint import pprint

class Game:
    def __init__(self):
        print("Initialize Game")
        self.gameBoard=[]
        self.gameloop()
        

    def printBoard(self):
        print("Printing Game Board here")
        print("   A    B    C    D    E    F    G    H  ")
        print("1\n\n2\n\n3\n\n4\n\n5\n\n6\n\n7\n\n8\n\n")


        
        pprint(self.gameBoard)
        

    def generateStartingBoard(self):
        print("Generating Starting Board")
        n = 8
        m = 8
        self.gameBoard = [[" "] * m for i in range(n)]
        whitePieces="RKBQOBKR"
        blackPieces="rkbqobkr"
        for i in range(0,8):
            self.gameBoard[0][i] = blackPieces[i]
            self.gameBoard[7][i] = whitePieces[i]
        for i in range(0,8):
            self.gameBoard[1][i] = "p"
            self.gameBoard[6][i] = "P"
        
        
        

    def gameloop(self):
        while True:
            self.generateStartingBoard()
            self.printBoard()
            break
Game()
