import os, pygame, sys;
os.system('cls'); #?Para borrar la consola

pygame.init(); #*Inicializa la libreria




#*Crear ventana de juego: 
""" screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN) """ 

screen = pygame.display.set_mode((1000,800));

#* Bucle principal

while (True): #*Ejecuta un bucle infinito para que el juego pueda correr
    for evento in pygame.event.get(): #*Durante cada frame o iteracion comprueba que el usuario no salga.
        if (evento.type == pygame.QUIT):
            sys.exit();
            
            
            
            
    
            
    
    #*Flujo del Juego
    
    pygame.display.flip() #*Actualiza la pantalla durante cada frame o iteracion del bucle