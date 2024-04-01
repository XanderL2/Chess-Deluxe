from modules.chess_board import ChessBoard
import pygame; 


#Animations and loading cover.

class UserInterfaceUI:

    # Constructor
    def __init__(self, background):
        self.background = background
        self.chessBoard = ChessBoard();

    # Méthods
    def Load_background(self):
        return pygame.image.load(self.background).convert()

    def Text(self,screen, text, color, size, coordinates):

        font_text = pygame.font.Font("./Resources/Fonts/Fresco Stamp.ttf", size)
        text = font_text.render(text, True, color)

        return screen.blit(text, coordinates)

    def FlashingAnimation (self, max, min, radius, fadeIn):
        if radius[0] >= max: fadeIn[0] = False
        if radius[0] <= min: fadeIn[0] = True
        radius[0] += 5 if fadeIn[0] else -5

    def ResetValues(self, radius, fadeIn):
        radius[0] = 0; 
        fadeIn[0] = True;

    def OldAnimation(self, radius, fadeIn, screen, background):

        background = pygame.image.load(background).convert()

        if(fadeIn[0]): radius[0] += 8;
        if(radius[0] >= 650): fadeIn[0] = False;
        if(fadeIn[0] == False): 

            screen.blit(background, (0, 0));
            self.chessBoard.posiciones_iniciales()
            self.chessBoard.dibujar_tablero(screen, 83, 33 )
            radius[0] -=  8;

        if(radius[0] <= 0): radius[0] = 0; 

    def AnimationCircle(self, radius, screen):
        pygame.draw.circle(screen, (0, 0, 0), (512, 320), radius)
