class Dron:
    
    distanciaXActual = 0
    distanciaYActual = 0

    
    def __init__(self, ID, tipo, color, tamano, comms):
        self.ID = ID
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
        self.rango = rango

    def volar(self,distancia, altura):
        try:
            print(f"El dron volara a {distancia}m en X y {altura}m en Y")
            self.distanciaXActual = distancia
            self.distanciaYActual = altura
        except:
            print("Revisa el valor ingresado de movimiento")

    def hablar(self):
        print(f"{self.ID} tiene un rango de {rango}m.")
