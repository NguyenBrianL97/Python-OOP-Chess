from abc import ABC, abstractmethod

class Piece(ABC):
    white=True 
    @abstractmethod
    def isWhite(self):
        pass
    def canMove(self):
        pass
    
class Pawn(Piece):
    def isWhite(self):
        print("hi")
        print(self.white)
    def canMove(self):
        pass
        
        
class Knight(Piece):
    def isWhite(self):
        print("hi")
        print(self.white)
  
  
x = Pawn()
x.isWhite()
