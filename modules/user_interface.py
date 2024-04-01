import pygame; 

class User_Interface_UI:
    # Constructor de la clase
    def __init__(self, background):
        self.background = background

    # Funciones o métodos de la clase
    def load_background(self):
        return pygame.image.load(self.background).convert()

    def text(self,screen, palabras, color, size, coordenadas):

        font_text = pygame.font.Font("./Resources/Fonts/Fresco Stamp.ttf", size)
        text = font_text.render(palabras, True, color)

        return screen.blit(text, coordenadas)

   
    
    def animation_init(self, radio, screen):
         pygame.draw.circle(screen, (0,0,0), (512,320),radio);
  