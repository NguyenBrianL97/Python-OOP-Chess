import Piece

class Spot:
    piece=None
    def __init__(self, piece, x, y):
        self.setPiece(piece); 
        self.y=y; 
        self.x=x;
    def setPiece(self, piece):
        self.piece=piece
        

chesspiece=Piece.Knight()

x = Spot(chesspiece,1,1)
print(x.x,x.y,x.piece.isWhite())9
