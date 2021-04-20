class Vehiculo():
    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        
    def descri(self):
        print(f"\nMarca: {self.marca}\nColor: {self.color}  Cantidad de ruedas: {self.ruedas}")


#miAuto = Vehiculo("Pontiac","Rojo", 4)
#miAuto.descri()

class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, marca_coche, color_coche, ruedas_coche): 

        super().__init__(marca_coche, color_coche, ruedas_coche)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def descri(self):
        super().descri()
        print(f"Velocidad: {self.velocidad}  Cilindrada: {self.cilindrada}")



class Bicicleta(Vehiculo):
    def __init__(self, tipo, marca_bici, color_bici, ruedas_bici):

        super().__init__(marca_bici, color_bici, ruedas_bici)
        self.tipo = tipo
    def descri(self):
        super().descri()
        print(f"Tipo: {self.tipo}")



class Camioneta(Coche, Vehiculo):
    def __init__(self, carga, cilindrada_camioneta, velocidad_camioneta, marca_camioneta, color_camioneta, ruedas_camioneta):

        super().__init__(cilindrada_camioneta, velocidad_camioneta, marca_camioneta, color_camioneta, ruedas_camioneta)
        self.carga = carga
    def descri(self):
        super().descri()
        print(f"Carga: {self.carga}")



class Moto(Bicicleta, Vehiculo):

    def __init__(self, velocidad_moto, cilindrada_moto, tipo_moto, marca_moto, color_moto, ruedas_moto):
        super().__init__(marca_moto, tipo_moto, color_moto, ruedas_moto)
        self.velocidad_moto = velocidad_moto
        self.cilindrada_moto = cilindrada_moto

    def descri(self):
        super().descri()
        print(f"Velocidad: {self.velocidad_moto}  Cilindrada: {self.cilindrada_moto}")




#miAuto = Vehiculo("Pontiac","Rojo", 4)
#miAuto.descri()

miAuto = Coche("150 km/h", "6 cilindros", "Pontiac", "Rojo", 4)
miAuto.descri()


miBici = Bicicleta("Urbana", "Olmo", "Verde", 2) #siempre empezar de lo mas lejos a los mas de arriba.
miBici.descri()


miCamioneta = Camioneta("150 toneladas", "120 km/h", "6 cilindros", "Volkswagen","Azul", 12 )
miCamioneta.descri()

miMoto = Moto("170 km/h", "12 cilindros", "Harley Davidson", "Deportiva", "Gris", 2)
miMoto.descri()