from modules.piezas import Pieces 
import pygame;


class ChessBoard:

    # Constructor de la clase:
    def __init__(self):
        self.board = (
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]
        )

    def DashboardInstances(self, row, color):
        self.board[row][0] =  Pieces("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")
        self.board[row][1] =  Pieces("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.board[row][2] =  Pieces("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.board[row][3] =  Pieces("Reina", color, f"./Resources/Images/Pieces/{color}/Reina {color}.png")
        self.board[row][4] =  Pieces("Rey", color, f"./Resources/Images/Pieces/{color}/Rey {color}.png")
        self.board[row][5] =  Pieces("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.board[row][6] =  Pieces("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.board[row][7] =  Pieces("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")

    def InitialPosition(self):

        for i in range(len(self.board)):

            if i == 0:
                self.DashboardInstances(i, "Blanco")

            if i == 7:
                self.DashboardInstances(i, "Negro")


            for j in range(len(self.board[i])):

                if i == 1:
                    self.board[i][j] =  Pieces("Peon", "Blanco", "./Resources/Images/Pieces/Blanco/Peon Blanco.png")

                elif i == 6:
                    self.board[i][j] =  Pieces("Peon", "Negro", "./Resources/Images/Pieces/Negro/Peon Negro.png")


    def drawBoard(self, screen, x, y):
        squareSize= 63

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                piece = self.board[i][j]

                if isinstance(piece,  Pieces):
                    pos = (x + j * squareSize, y + i * squareSize)
                    screen.blit(pygame.image.load(piece.GetImage()), pos)


