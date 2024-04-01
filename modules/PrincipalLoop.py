from modules.chessBoard import ChessBoard
import sys, pygame;


class GameloopPrincipal:

    #* Constructor
    def __init__(self, userInterface):
        self.userInterface = userInterface 
        self.chess_board = ChessBoard();

    
    
    
    #* Principal Method
    def StartGame(self):

        #* Variables
        screen = pygame.display.set_mode((1024, 640))
        fps = pygame.time.Clock()
        background = self.userInterface.LoadBackground()

        start_game = False;
        efecto = [0];
        aumento = [True];
        pulsacion = True;      
        
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
                    if(pulsacion): 
                        self.userInterface.ResetValues(efecto, aumento);                     
                        pulsacion = False;


            #*Flujo Principal

            if start_game:
                

                self.userInterface.OldAnimation(efecto, aumento, screen, "./Resources/Images/FONDO.png")
                self.userInterface.AnimationCircle(efecto[0], screen)
               

                
                #?Logica de Movimiento y Gameplay
                
                
                
               

            else:
                #Cover
                screen.blit(background, (0, 0))
                self.userInterface.FlashingAnimation(255, 0, efecto, aumento);
                self.userInterface.Text(screen, "P U L S A   P A R A   I N I C I A R", (efecto[0], 0, 0), 70, (80, 500))  


            pygame.display.flip()
            fps.tick(60)
