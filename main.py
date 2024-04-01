#?Librerias
import os, pygame;

from modules.userInterface import UserInterfaceUI;
from modules.PrincipalLoop import GameloopPrincipal;


os.system("clear"); 


#?Inicalizacion del Juego   
pygame.init();
pygame.mixer.init();


userInterfaceInstance= UserInterfaceUI("./Resources/Images/BACKGROUND_CHESS.jpg")
chess = GameloopPrincipal(userInterfaceInstance)
chess.StartGame()
