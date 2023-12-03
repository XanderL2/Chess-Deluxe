#?Librerias
import os, pygame, sys, modules;
from modules import User_Interface_UI, game_loop_principal, Piezas; 
os.system('cls'); 



#?Inicalizacion del Juego   


pygame.init();

user_interface_instance = User_Interface_UI("./Resources/Images/BACKGROUND CHESS.jpg"); 

ajedrez = game_loop_principal(user_interface_instance)

ajedrez.start_game()



