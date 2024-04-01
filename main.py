#?Librerias
import os, pygame;

from modules.user_interface import UserInterfaceUI;
from modules.loop_principal import GameloopPrincipal;


os.system("clear"); 


#?Inicalizacion del Juego   
pygame.init();
pygame.mixer.init();


userInterfaceInstance= UserInterfaceUI("./Resources/Images/BACKGROUND_CHESS.jpg")
ajedrez = GameloopPrincipal(userInterfaceInstance)
ajedrez.Start_game()
