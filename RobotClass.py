class Robot:
    
    distanciaActual = (0,0)

    def __init__(self, ID, tipo, color, tamano, comms):
        self.ID = ID
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
        self.comms = comms
