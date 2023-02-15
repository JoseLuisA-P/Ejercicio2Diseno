class Robot:
    
    distanciaActual = (0,0)

    def __init__(self, ID, tipo, color, tamano, comms):
        self.ID = ID
        self.tipo = tipo
        self.color = color
        self.tamano = tamano
        self.comms = comms

    def mover(self,distancia):
        try:
            print(f"El robot se movera a {distancia[0]}m en X y {distancia[1]}m en Y")
            self.distanciaActual = distancia
        except:
            print("Revisa el valor ingresado de movimiento")

    def hablar(self):
        print(f"{self.ID} esta tratando de comunicarte algo por {self.comms}")
    
    def sensores(self):
        try:
            mag = self.distanciaActual[0] + self.distanciaActual[1]
            print(f"Ha detectado un objeto a {mag}")
        except:
            print("Revisa la distancia ingresada")

    def __str__(self):
        return f"\nEste es {self.ID}\n{self.tipo}\n{self.color}\n{self.tamano}\n{self.comms}"
