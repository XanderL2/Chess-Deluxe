from modules.piezas import Piezas
import pygame;


class Chess_Board:
    # Constructor de la clase:
    def __init__(self):
        self.tablero_matriz = (
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]
        )

    def instancias_tablero(self, fila, color):
        self.tablero_matriz[fila][0] = Piezas("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")
        self.tablero_matriz[fila][1] = Piezas("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.tablero_matriz[fila][2] = Piezas("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.tablero_matriz[fila][3] = Piezas("Reina", color, f"./Resources/Images/Pieces/{color}/Reina {color}.png")
        self.tablero_matriz[fila][4] = Piezas("Rey", color, f"./Resources/Images/Pieces/{color}/Rey {color}.png")
        self.tablero_matriz[fila][5] = Piezas("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.tablero_matriz[fila][6] = Piezas("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.tablero_matriz[fila][7] = Piezas("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")

    def posiciones_iniciales(self):

        for i in range(len(self.tablero_matriz)):

            if i == 0:
                self.instancias_tablero(i, "Blanco")

            if i == 7:
                self.instancias_tablero(i, "Negro")

            for j in range(len(self.tablero_matriz[i])):

                if i == 1:
                    self.tablero_matriz[i][j] = Piezas("Peon", "Blanco", "./Resources/Images/Pieces/Blanco/Peon Blanco.png")

                elif i == 6:
                    self.tablero_matriz[i][j] = Piezas("Peon", "Negro", "./Resources/Images/Pieces/Negro/Peon Negro.png")

        """ for fila in self.tablero_matriz:
            print(fila) """

    def dibujar_tablero(self, screen, x, y):
        tam_cuadrado = 63

        for i in range(len(self.tablero_matriz)):
            for j in range(len(self.tablero_matriz[i])):
                pieza = self.tablero_matriz[i][j]

                if isinstance(pieza, Piezas):
                    pos = (x + j * tam_cuadrado, y + i * tam_cuadrado)
                    screen.blit(pygame.image.load(pieza.obtener_imagen()), pos)

