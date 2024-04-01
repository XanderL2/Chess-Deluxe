from modules.chess_board import Chess_Board
import sys, pygame;


class game_loop_principal:

    #* Constructor
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.chess_board = Chess_Board();

    
    
    #* Principal Method
    def start_game(self):

        #* Variables
        screen = pygame.display.set_mode((1024, 640))
        fps = pygame.time.Clock()
        background = self.user_interface.Load_background()

        start_game = False;
        efecto = [0];
        aumento = [True];

        transition = True;      
        
        #*Effects:
        pygame.mixer.init();
        pygame.mixer.music.load("./Resources/Soundtrack/undertale_soundrack.wav")
        pygame.mixer_music.play(-1);


        
        
    
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit();
                elif evento.type == pygame.KEYDOWN:
                    start_game = True;
                    self.user_interface.ResetValues(efecto, aumento)                    
                    


            #* Flujo Principal
            #?Animaciones de Carga y Dibujado de Tablero
            if start_game:
                
                
                
                self.user_interface.OldAnimation(efecto, aumento)
                self.user_interface.AnimationCircle(efecto[0], screen)
        

                if(efecto[0] == 0):
                    background = pygame.image.load("./Resources/Images/FONDO.png").convert()
                    screen.blit(background, (0, 0));

                print(efecto[0])
                                   


               
               
               
               
               
               
                
                
                # if animation: 
                #     efecto += 5
                    
                #     if efecto >= 600:
                #         animation = False
                #         background = pygame.image.load("./Resources/Images/FONDO.png").convert()
                #         screen.blit(background, (0, 0));
                # else:
                #     efecto -= 10
                #     if efecto <= 0:
                #         efecto = 0
                
                
                 
                # if(transition):  
                #     screen.blit(background, (0, 0));
                #     self.user_interface.animation_init(efecto, screen)
                    
                #     if(efecto == 0):
                #         transition = False;
                        
                # else:
                #     self.chess_board.posiciones_iniciales()
                #     self.chess_board.dibujar_tablero(screen, 83, 33 )
                
                #?Logica de Movimiento y Gameplay
                
                
                
               

            else:
                #Cover
                screen.blit(background, (0, 0))
                self.user_interface.FlashingAnimation(255, 0, efecto, aumento);
                self.user_interface.Text(screen, "P U L S A   P A R A   I N I C I A R", (efecto[0], 0, 0), 70, (80, 500))  


            fps.tick(60)
            pygame.display.flip()


