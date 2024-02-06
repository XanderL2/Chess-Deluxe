

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
