#?Librerias
import os, pygame, sys, modules;
os.system('cls'); 



#?Inicalizacion del Juego
pygame.init(); 

#?Crear ventana de juego: 

screen = pygame.display.set_mode((1024,640)); #*Definimos el tamaño de la pantalla
fps = pygame.time.Clock(); #*Usamos el metodo clock para establecer los FPS
background = pygame.image.load("./Resources/Images/BACKGROUND CHESS.jpg").convert(); 
start_game = False; 

zero_var = 0  #*Variable inicializada en 0
increasing = True





#? Bucle principal

while (True): #*Ejecuta un bucle infinito para que el juego pueda correr
    for evento in pygame.event.get(): #*Durante cada frame o iteracion comprueba que el usuario no salga.
        if (evento.type == pygame.QUIT):
            sys.exit();
        elif(evento.type == pygame.KEYDOWN):
            start_game = True;
        
            
        
    #*Flujo del Juego
    
    if(start_game == True):
        
        
        if(increasing):
            
            if(zero_var >= 1000):
                zero_var = 0;
                increasing = False;
        else:
            zero_var +=1; 
        
        
            
        print(zero_var);
            
            
        """ modules.animation_cierre(screen);      """
        
        
        """ background = pygame.image.load("./Resources/Images/FONDO.png").convert(); 
        screen.blit(background, (0, 0)); """
       
       
        
        
        
    else:
        
        print("Paso por el else")
        if (increasing):
            zero_var += 9;
            if (zero_var >= 255):
                zero_var = 255
                increasing = False
        else:
            
            zero_var -= 9;
            if (zero_var <= 0):
                zero_var = 0
                increasing = True
    
        modules.text("P U L S A   P A R A   I N I C I A R", (zero_var, 0, 0), 70, (80, 500));
        
        
    
    
    







             

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    fps.tick(60)
    pygame.display.flip() #*Actualiza la pantalla durante cada frame o iteracion del bucle
