#?Librerias
import os, pygame;
from modules import User_Interface_UI, game_loop_principal;
os.system('cls'); 



#?Inicalizacion del Juego   


pygame.init();
pygame.mixer.init();

user_interface_instance = User_Interface_UI("./Resources/Images/BACKGROUND CHESS.jpg"); 

ajedrez = game_loop_principal(user_interface_instance)

ajedrez.start_game()


print("xd");
