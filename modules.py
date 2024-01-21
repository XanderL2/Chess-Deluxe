import pygame, sys;

class game_loop_principal:
    #* Constructor de la clase
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.chess_board = Chess_Board();
    #* Funciones o métodos de la clase
    def start_game(self):
        #* Variables
        screen = pygame.display.set_mode((1024, 640))
        fps = pygame.time.Clock()
        background = self.user_interface.load_background()
        start_game = False;
        efecto = 0;
        aumento = True;
        animation = True;
        transition = True;
        
        #*Effects:
        #?Soundtrack
        pygame.mixer.init();
        pygame.mixer.music.load("./Resources/Music and effects/SoundtTrack/Undertale_Soundrack.wav");
        pygame.mixer_music.play(-1);

        
        
    
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit();
                elif evento.type == pygame.KEYDOWN:
                    
                    start_game = True;

            #* Flujo Principal
            #?Animaciones de Carga y Dibujado de Tablero
            if start_game:
                
                if animation: 
                    efecto += 5
                    
                    if efecto >= 600:
                        animation = False
                        background = pygame.image.load("./Resources/Images/FONDO.png").convert()
                        screen.blit(background, (0, 0));
                else:
                    efecto -= 10
                    if efecto <= 0:
                        efecto = 0
                      
                if(transition):  
                    screen.blit(background, (0, 0));
                    self.user_interface.animation_init(efecto, screen)
                    
                    if(efecto == 0):
                        transition = False;
                        
                else:
                    self.chess_board.posiciones_iniciales()
                    self.chess_board.dibujar_tablero(screen, 83, 33 )
                
                
                
                #?Logica de Movimiento y Gameplay
                
                
                
                
                
                
                
                

            else:
                screen.blit(background, (0, 0))
                print("else")

                if aumento:
                    efecto = self.user_interface.aumento(efecto)
                    if efecto >= 255:
                        efecto = 255
                        aumento = False
                else:
                    efecto -= 12
                    if efecto <= 0:
                        efecto = 0
                        aumento = True

                print(efecto)
                self.user_interface.text(screen, "P U L S A   P A R A   I N I C I A R", (efecto, 0, 0), 70, (80, 500))  


            fps.tick(60)
            pygame.display.flip()



class User_Interface_UI:
    # Constructor de la clase
    def __init__(self, background):
        self.background = background

    # Funciones o métodos de la clase
    def load_background(self):
        return pygame.image.load(self.background).convert()

    def text(self,screen, palabras, color, size, coordenadas):
        font_text = pygame.font.Font("./Resources/Fonts/Fresco Stamp.ttf", size)
        text = font_text.render(palabras, True, color)
        return screen.blit(text, coordenadas)

    def aumento(self, numero):
        return numero + 10;
    
    def reseteo_numero(self):
        return 0;
        
    
    def animation_init(self, radio, screen):
         pygame.draw.circle(screen, (0,0,0), (512,320),radio);
               
    
class Chess_Board:
    # Constructor de la clase:
    def __init__(self):
        self.tablero_matriz = (
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]
        )

    def instancias_tablero(self, fila, color):
        self.tablero_matriz[fila][0] = Piezas("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")
        self.tablero_matriz[fila][1] = Piezas("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.tablero_matriz[fila][2] = Piezas("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.tablero_matriz[fila][3] = Piezas("Reina", color, f"./Resources/Images/Pieces/{color}/Reina {color}.png")
        self.tablero_matriz[fila][4] = Piezas("Rey", color, f"./Resources/Images/Pieces/{color}/Rey {color}.png")
        self.tablero_matriz[fila][5] = Piezas("Alfil", color, f"./Resources/Images/Pieces/{color}/Alfil {color}.png")
        self.tablero_matriz[fila][6] = Piezas("Caballo", color, f"./Resources/Images/Pieces/{color}/Caballo {color}.png")
        self.tablero_matriz[fila][7] = Piezas("Torre", color, f"./Resources/Images/Pieces/{color}/Torre {color}.png")

    def posiciones_iniciales(self):

        for i in range(len(self.tablero_matriz)):

            if i == 0:
                self.instancias_tablero(i, "Blanco")

            if i == 7:
                self.instancias_tablero(i, "Negro")

            for j in range(len(self.tablero_matriz[i])):

                if i == 1:
                    self.tablero_matriz[i][j] = Piezas("Peon", "Blanco", "./Resources/Images/Pieces/Blanco/Peon Blanco.png")

                elif i == 6:
                    self.tablero_matriz[i][j] = Piezas("Peon", "Negro", "./Resources/Images/Pieces/Negro/Peon Negro.png")

        """ for fila in self.tablero_matriz:
            print(fila) """

    def dibujar_tablero(self, screen, x, y):
        tam_cuadrado = 63

        for i in range(len(self.tablero_matriz)):
            for j in range(len(self.tablero_matriz[i])):
                pieza = self.tablero_matriz[i][j]

                if isinstance(pieza, Piezas):
                    pos = (x + j * tam_cuadrado, y + i * tam_cuadrado)
                    screen.blit(pygame.image.load(pieza.obtener_imagen()), pos)

           
class Piezas:
    def __init__(self, tipo_pieza, color, image_piece):
        self.tipo_pieza = tipo_pieza
        self.color_pieza = color
        self.image_piece = image_piece
        self.fila_actual = None
        self.columna_actual = None

    def obtener_color(self):
        return self.color_pieza

    def obtener_tipo(self):
        return self.tipo_pieza

    def obtener_imagen(self):
        return self.image_piece

    def obtener_posicion_actual(self):
        return self.fila_actual, self.columna_actual

    def establecer_posicion_actual(self, fila, columna):
        self.fila_actual = fila
        self.columna_actual = columna

    def movimientos_posibles(self):
        pass

    def movimiento_valido(self, destino):
        pass

    def realizar_movimiento(self, destino):
        pass

    def info_pieza(self):
        print(f"Color: {self.color_pieza}, Tipo: {self.tipo_pieza}")

        
class player:
    def __init__(self, piezas_activas, score):
        self.piezas_activas = piezas_activas;
        self.score = score;
        
    
class estado_juego:
    def __init__(self, name):
        self.name = name;


















""" def animation_inicio(screen, radio):
    pygame.draw.circle(screen, (0,0,0), (512,320),radio)
    
    

def animation_cierre(screen, radio):
    pygame.draw.circle(screen, (0,0,0), (512, 324),radio)



def text(palabras, color, size, coordenadas):
    
    font_text = pygame.font.Font("./Resources/Fonts/Fresco Stamp.ttf",size);
    text = font_text.render(palabras, True, color);
        
    return screen.blit(text, coordenadas);
    
    









def chess_board():
    tablero = [
        ["", "", "", "", "", "", "",""],
        ["p", "p", "p", "p", "p", "p", "p","p"],
        ["", "", "", "", "", "", "",""],
        ["", "", "", "", "", "", "",""],
        ["", "", "", "", "", "", "",""],
        ["", "", "", "", "", "", "",""],
        ["p", "p", "p", "p", "p", "p", "p","p"],
        ["", "", "", "", "", "", "",""]]; """
    
    

    
    
