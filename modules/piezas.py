class Pieces:
    def __init__(self, type , color, imagePiece):
        self.type = type  
        self.pieceColor = color
        self.imagePiece = imagePiece
        self.currentRow = None
        self.currentColumn = None

    def GetColor(self):
        return self.pieceColor;

    def GetType(self):
        return self.type;

    def GetImage(self):
        return self.imagePiece;

    def GetCurrentPosition(self):
        return self.currentRow, self.currentColumn;

    def SetPosition(self, row, column):
        self.currentRow = row; 
        self.currentColumn = column;

    def PossibleMovements(self):
        pass

    def movimiento_valido(self, destino):
        pass

    def realizar_movimiento(self, destino):
        pass

    def PieceInformation(self):
        print(f"Color: {self.pieceColor}, Tipo: {self.type}")
