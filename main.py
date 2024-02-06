#?Librerias
import os, pygame;
from user_interface import User_Interface_UI;
from loop_principal import game_loop_principal;
os.system("clear"); 



#?Inicalizacion del Juego   


pygame.init();
pygame.mixer.init();


user_interface_instance = User_Interface_UI("./Resources/Images/BACKGROUND_CHESS.jpg"); 

ajedrez = game_loop_principal(user_interface_instance)

ajedrez.start_game()


