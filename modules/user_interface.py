import pygame; 

#Animations and loading cover.

class User_Interface_UI:

    # Constructor
    def __init__(self, background):
        self.background = background

    # Méthods
    def Load_background(self):
        return pygame.image.load(self.background).convert()

    def Text(self,screen, palabras, color, size, coordenadas):

        font_text = pygame.font.Font("./Resources/Fonts/Fresco Stamp.ttf", size)
        text = font_text.render(palabras, True, color)

        return screen.blit(text, coordenadas)

    def FlashingAnimation (self, max, min, efecto, aumento):
        if efecto[0] >= max: aumento[0] = False
        if efecto[0] <= min: aumento[0] = True
        efecto[0] += 5 if aumento[0] else -5

    def ResetValues(self, efecto, aumento):
        efecto[0] = 0; 
        aumento[0] = True;

    def OldAnimation(self, efecto, aumento):
        if(aumento[0]): efecto[0]+= 5;
        if(efecto[0] == 600): aumento[0] = False;
        if(aumento[0] == False): efecto[0] -= 5;
        if(efecto[0] <= 0):
            efecto[0] = 0; 


        
  
    
    def AnimationCircle(self, radio, screen):
         pygame.draw.circle(screen, (0,0,0), (512,320),radio);
  